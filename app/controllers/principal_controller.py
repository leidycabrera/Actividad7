from flask import render_template, session, redirect, url_for, request, jsonify
from app import app
from werkzeug.security import generate_password_hash
from datetime import timedelta
from app.models.persona import Persona
from app.models.tipo_persona import TipoPersona
from app.models.paquete import Paquete

@app.route('/')
def index():
    if 'id_persona' not in session:
        return redirect(url_for('login'))
    rol = Persona.find_by_id(session.get('id_persona'))
    cliente = Persona.get_by_tipoPersona('Cliente')
    paquetes = Paquete.get_by_idpersona(session.get('id_persona'))
    options_cliente = ''
    options_paquete = ''
    for item in cliente:
        options_cliente += f'<option value="{item["idpersona"]}">{item["nombre_persona"]}</option>'

    for item in paquetes:
        options_paquete += f'<option value="{item["idpaquete"]}">{item["nombre_paquete"]}</option>'

    if rol['nombre_tipo'] == 'Administrador' or rol['nombre_tipo'] == 'Recepcionista':
        vista = '''<div class="container">
                        <h1>Bienvenid@</h1>
                        <p>Selecciona una opción para ver los datos de:</p>
                        <div class="row">
                            <div class="col-md-11">
                                <select id="filtro_admin" class="form-control">
                                    <option value="Distribuidor">Distribuidores</option>
                                    <option value="Cliente">Clientes</option>
                                </select>
                            </div>
                        <div class="col-md-1">
                            <input type="submit" id="filtrar_clientes" class="btn btn-personalizado" value="Filtrar">
                        </div>
                        </div>
                    </div>'''
    elif rol['nombre_tipo'] == 'Empacador':
        vista = '''<div class="container">
                        <h1>Bienvenid@</h1>
                        <p>Selecciona el comprador para generar su etiqueta:</p>
                        <div class="row">
                            <div class="col-md-11">
                                <select id="select_generar" class="form-control">
                                '''+options_cliente+'''
                                </select>
                            </div>
                        <div class="col-md-1">
                            <input type="submit" id="generar_etiqueta" class="btn btn-personalizado" value="Generar">
                        </div>
                        </div>
                    </div>'''
    elif rol['nombre_tipo'] == 'Cliente' or rol['nombre_tipo'] == 'Distribuidor':
        vista = '''<div class="container">
                        <h1>Bienvenid@</h1>
                        <p>Selecciona un paquete:</p>
                        <div class="row">
                            <div class="col-md-11">
                                <select id="select_paquetes" class="form-control">
                                '''+options_paquete+'''
                                </select>
                            </div>
                        <div class="col-md-1">
                            <input type="submit" id="filtrar_paquete" class="btn btn-personalizado" value="Rastrear">
                        </div>
                        </div>
                    </div>'''
    elif rol['nombre_tipo'] == 'Transportador':
        vista = '''<div class="container">
                        <h1>Bienvenid@</h1>
                        <p>Selecciona una opción:</p>
                        <div class="row">
                            <div class="col-md-11">
                                <select id="filtro_trans" class="form-control">
                                    <option value="paquetes">Ver paquetes</option>
                                    <option value="Cliente">Ver clientes</option>
                                    <option value="Distribuidor">Ver distribuidores</option>
                                </select>
                            </div>
                        <div class="col-md-1">
                            <input type="submit" id="filtrar_datos_traspo" class="btn btn-personalizado" value="Filtrar">
                        </div>
                        </div>
                    </div>'''
    else:
        vista = f"Not found"

    return render_template('index.html', vista=vista, rol=rol)

@app.route('/filtrar_clientes', methods=['POST'])
def filtrar_clientes():
    option = request.form.get('option')
    data = Persona.get_by_tipoPersona(option)
    id_tipo = TipoPersona.getId_by_type(option)
    idtipo_persona= id_tipo[0]['idtipo_persona']
    return render_template('form.html', option=option, data=data, idtipo_persona=idtipo_persona)

@app.route('/guardar_persona', methods=['POST'])
def guardar_persona():
    try:
        idpersona = request.form.get('idpersona')
        nombre = request.form.get('nombre_persona')
        apellido = request.form.get('apellido')
        docidentidad = request.form.get('docidentidad')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        correo = request.form.get('correo')
        idtipo_persona = request.form.get('idtipo_persona')
        username = nombre[0]+apellido
        password = generate_password_hash('123456')
        Persona.save(idpersona, nombre, apellido, docidentidad, telefono, direccion, correo, username, password, idtipo_persona)
        return jsonify({"success": True, "message": "Registro guardado exitosamente"}), 200
    except Exception as e:
        print(f"Error al guardar persona: {e}")
        return jsonify({"error": False, "message": "Error al guardar el registro"}), 500

@app.route('/obtener_persona/<int:id>', methods=['GET'])
def obtener_persona(id):
    persona = Persona.find_by_id(id)
    if persona:
        return jsonify({
            'idpersona': persona['idpersona'],
            'nombre_persona': persona['nombre_persona'],
            'apellido': persona['apellido'],
            'docidentidad': persona['docidentidad'],
            'telefono': persona['telefono'],
            'direccion': persona['direccion'],
            'correo': persona['correo'],
            'idtipo_persona': persona['idtipo_persona'],
            'nombre_tipo': persona['nombre_tipo']
        })
    else:
        return jsonify({'error': 'Persona no encontrada'}), 404

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_persona(id):
    persona = Persona.delete(id)
    if persona == True:
        return jsonify({"success": True, "message": "Registro eliminado exitosamente"}), 200
    else:
        return jsonify({"success": True, "message": "Error al eliminare l registro"}), 500
    
@app.route('/generar_etiqueta', methods=['POST'])
def generar_etiqueta():
    option = request.form.get('option')
    persona = Persona.find_by_id(option)
    if not persona:
        return "Persona no encontrada", 404
    
    return render_template('etiqueta.html', persona=persona)

@app.route('/filtrar_paquete', methods=['POST'])
def filtrar_paquete():
    option = request.form.get('option')
    data = Paquete.get_all_byId(option)
    return render_template('form_paquete.html', option=option, data=data)

@app.route('/obtener_paquete/<int:id>', methods=['GET'])
def obtener_paquete(id):
    paquete = Paquete.get_package_byId(id)
    if paquete:
        return jsonify({
            'idpaquete': paquete['idpaquete'],
            'nombre_paquete': paquete['nombre_paquete'],
            'fecha_entrega': paquete['fecha_entrega'].strftime('%Y-%m-%d'),
            'hora_entrega': str(paquete['hora_entrega'])
        })
    else:
        return jsonify({'error': 'Paquete no encontrado'}), 404
    
@app.route('/editar_paquete', methods=['POST'])
def editar_paquete():
    try:
        idpaquete = request.form.get('idpaquete')
        fecha_entrega = request.form.get('fecha_entrega')
        hora_entrega = request.form.get('hora_entrega')
        ## Valida si el paquete ya se envió
        estado_paquete = Paquete.get_all_byId(idpaquete)
        if estado_paquete[0]['nombre_fase'] == 'Empacando' or estado_paquete[0]['nombre_fase'] == 'Empacado':
            response = Paquete.edit(idpaquete, fecha_entrega, hora_entrega)
            if response:
                return jsonify({"success": True, "message": "Fechas u horarios de entrega modificados exitosamente"}), 200
            else:
                return jsonify({"success": True, "message": "Error en la actuialización"}), 200
        else:
            return jsonify({"success": True, "message": "No se puede modificar la fecha u horario de envio porque el paquete se encuentra en estado: "+estado_paquete[0]['nombre_fase'] }), 200
    except Exception as e:
        print(f"Error al guardar persona: {e}")
        return jsonify({"error": False, "message": "Error al editar el paquete"}), 500
    
@app.route('/filtrar_datos_transportador', methods=['POST'])
def filtrar_datos_transportador():
    option = request.form.get('option')
    print(option)
    if option == 'paquetes':
        data = Paquete.get_all_packages()
        return render_template('form_paquete.html', option=option, data=data)
    elif option == 'Cliente' or option == 'Distribuidor':
        data = Persona.get_by_tipoPersona(option)
        id_tipo = TipoPersona.getId_by_type(option)
        idtipo_persona= id_tipo[0]['idtipo_persona']
        return render_template('form.html', option=option, data=data, idtipo_persona=idtipo_persona)