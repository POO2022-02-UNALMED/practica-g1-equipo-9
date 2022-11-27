import tkinter as tk
from tkinter import *
from tkinter import messagebox
from reagendarCita import reagendarCita
from solicitarExamen import solicitarExamen
from solicitarCita import solicitarCita 
from mostrarDiagnostico import mostrarDiagnostico
from solicitarEntregaMedicamentos import solicitarEntregaMedicamentos
from crearDiagnostico import crearDiagnostico
from pagarConsulta import pagarConsulta
from pagarEntrega import pagarEntrega
from baseDatos.Serializador import serializar
from baseDatos.Deserializador import deserializar
from datetime import datetime
from PIL import Image, ImageTk
from excepciones.excepcionPresenciaArchivo import ExcepcionPresenciaArchivos
from excepciones.excepcionPresenciaImagenes import ExcepcionPresenciaImagenes

deserializar()
def inicializar():
    """
    
    from gestorAplicacion.personas.Administrador import Administrador
    from gestorAplicacion.personas.Medico import Medico
    from gestorAplicacion.personas.Paciente import Paciente
    from gestorAplicacion.Consultorio import Consultorio
    from gestorAplicacion.personas.tipoDocumento import tipoDocumento
    from gestorAplicacion.personas.tipoMedico import tipoMedico
    from gestorAplicacion.tipoCita import tipoCita
    from gestorAplicacion.Pago import Pago
    from gestorAplicacion.Cita import Cita
    from gestorAplicacion.Entrega import Entrega
    from gestorAplicacion.estadoEntrega import estadoEntrega
    from gestorAplicacion.registrosMedicos.Diagnostico import Diagnostico
    from gestorAplicacion.Medicamentos import Medicamentos
    from gestorAplicacion.tipoMedicamento import tipoMedicamento
    from gestorAplicacion.registrosMedicos.HistoriaClinica import HistoriaClinica
    
    fecha1 = datetime(2022, 10, 15, 12, 30)
    fecha2 = datetime(2022, 10, 15, 13, 00)
    fecha3 = datetime(2022, 10, 15, 13, 30)
    fecha4 = datetime(2022, 10, 15, 14, 00)
    fecha5 = datetime(2022, 10, 15, 14, 30)
    fecha6 = datetime(2022, 10, 15, 15, 00)
    fecha7 = datetime(2022, 10, 15, 15, 30)
    fecha8 = datetime(2022, 10, 16, 12, 30)
    fecha9 = datetime(2022, 10, 16, 13, 00)
    fecha10 = datetime(2022, 10, 16, 13, 30)
    fecha11 = datetime(2022, 10, 16, 14, 00)
    fecha12 = datetime(2022, 10, 16, 14, 30)
    fecha13 = datetime(2022, 10, 16, 15, 00)
    fecha14 = datetime(2022, 10, 16, 15, 30)
    nomina9 = datetime(2022, 9, 1, 00, 00)
    nomina10 = datetime(2022, 10, 1, 00, 00)
    
    Paciente1 = Paciente("Sara", "Marin", tipoDocumento.CEDULA, 1, 20, "Femenino", 2038487, "sama@gmail.com", "calle 36 #89 53", "SURA", None, True)
    Paciente2 = Paciente("Juan", "Pérez", tipoDocumento.CEDULA, 2, 30, "Masculino", 245687523, "juanper@gmail.com", "Carrera 68 # 54 12", "SURA", None, True)
    Paciente3 = Paciente("Camilo", "Martinez", tipoDocumento.CEDULA, 3, 24, "Masculino", 300762957, "mcm@gmail.com", "cra87#12-34", "SURA", None, True)
    
    medico1 = Medico("Susana", "Perez", tipoDocumento.CEDULA, 1000758374, 25, "Femenino", 1000758374, 
                 "susper@gmail.com", "Cra 77 #45 04", tipoCita.GENERAL, tipoMedico.BACTERIOLOGO, True)
    medico2 = Medico("Andres", "Lopez", tipoDocumento.CEDULA, 1254687950, 29, "Masculino", 1254687950, 
                 "andlop@gmail.com", "Calle 113 #55 05", tipoCita.GENERAL, tipoMedico.OPTOMETRA, True)
    medico3 = Medico("Mariana", "Garcia", tipoDocumento.CEDULA, 656502354, 28, "Femenino", 656502354, 
                 "margar@gmail.com", "Avenida 7 #8 07", tipoCita.GENERAL, tipoMedico.OPTOMETRA, True)
    medico4 = Medico("Mauricio", "Fernandez", tipoDocumento.CEDULA, 98765432, 60, "Masculino", 388030284,
                 "mp@hotmail.com", "carrera 78", tipoCita.AUDIOMETRIA, tipoMedico.FONOAUDIOLOGO, True)
    
    medico5 = Medico("María", "Mercedes", tipoDocumento.CEDULA, 154687, 29, "Masculino", 65426548, "marmer@gmail.com",
		  "Clle 77 #49 04", tipoCita.GENERAL, tipoMedico.GENERAL , False)
    medico6 = Medico("Alejandro", "Valencia", tipoDocumento.CEDULA, 9875642, 38, "Masculino", 236547898, 
                    "alval@gmail.com", "Carrera 111 #25 05", tipoCita.GENERAL, tipoMedico.PEDIATRA, False)
    medico7 = Medico("Valentina", "Gomez", tipoDocumento.CEDULA, 2154687, 26, "Femenino", 655984236,
                    "valgom,@gmail.com", "Avenida 70 #22 07", tipoCita.GENERAL, tipoMedico.BACTERIOLOGO, False)
    medico8 = Medico("David", "Herrera", tipoDocumento.CEDULA, 65498752, 50, "Masculino", 87630549,
		  "dherrera@hotmail.com", "Transversal 78 # 69 02", tipoCita.AUDIOMETRIA, tipoMedico.FONOAUDIOLOGO, False)
    medico9= Medico("Juan", "Calvo", tipoDocumento.CEDULA, 12354889, 65, "Masculino", 65698421,
		  "jcalvo@hotmail.com", "carrera 80 # 95 6", tipoCita.AUDIOMETRIA, tipoMedico.OPTOMETRA, False)
    medico5.setSueldo(70000)
    medico6.setSueldo(60000)
    medico7.setSueldo(60000)
    medico8.setSueldo(80000)
    medico9.setSueldo(80000)
    
    medico1.setNomina({nomina9 : Pago(None, medico1.getSueldo(), None, medico1, True), nomina10 : Pago(None, medico1.getSueldo(), None, medico1, True)})
    medico2.setNomina({nomina9 : Pago(None, medico2.getSueldo(), None, medico2, True), nomina10 : Pago(None, medico2.getSueldo())})
    medico3.setNomina({nomina9 : Pago(None, medico3.getSueldo(), None, medico3, True), nomina10 : Pago(None, medico3.getSueldo(), None, medico3, True)})
    medico4.setNomina({nomina9 : Pago(None, medico4.getSueldo(), None, medico4, True), nomina10 : Pago(None, medico4.getSueldo())})
    
    medico5.setNomina({nomina9 : Pago(None, medico5.getSueldo()), nomina10 : Pago(None, medico5.getSueldo())})
    medico6.setNomina({nomina9 : Pago(None, medico6.getSueldo()), nomina10 : Pago(None, medico6.getSueldo())})
    medico7.setNomina({nomina9 : Pago(None, medico7.getSueldo()), nomina10 : Pago(None, medico7.getSueldo())})
    medico8.setNomina({nomina9 : Pago(None, medico8.getSueldo()), nomina10 : Pago(None, medico8.getSueldo())})
    medico9.setNomina({nomina9 : Pago(None, medico9.getSueldo()), nomina10 : Pago(None, medico9.getSueldo())})
    
    consultorio1 = Consultorio(1, None, None, "Laboratorio", True)
    consultorio2 = Consultorio(2, None, None, "Consultorio Optometría", True)
    consultorio3 = Consultorio(3, None, None, "Consultorio Optometría", True)
    consultorio4 = Consultorio(4, None, None, "Consultorio Audiometría", True)
    
    consultorio5 = Consultorio(5, None, None, "Laboratorio", False)
    consultorio6 = Consultorio(6, None, None, "Consultorio Fonoaudología", False) 
    consultorio7 = Consultorio(7, None, None, "Consultorio Pediatria", False)
    consultorio8 = Consultorio(8, None, None, "Consultorio General", False)
    
    cita1 = Cita(1, Paciente1, "Un laboratorio", medico1, consultorio1, fecha1, None, tipoCita.LABORATORIO) 
    cita6 = Cita(6, Paciente3, "Un laboratorio", medico1, consultorio1, fecha4,None, tipoCita.LABORATORIO) 
    cita11 = Cita(11, Paciente2, "Un laboratorio", medico1, consultorio1, fecha5,None, tipoCita.LABORATORIO) 
    cita16 = Cita(16, None, "Un laboratorio", medico1, consultorio1, fecha6, None, tipoCita.LABORATORIO) 
    cita1.setPago(Pago(None, 15000, None, None, True))
    cita6.setPago(Pago(None, 15000));
    cita11.setPago(Pago(None, 15000))
		  
    cita2 = Cita(2, None, "Revisión visual", medico2, consultorio2, fecha1,None,  tipoCita.OPTOMETRIA) 
    cita3 = Cita(3,None, "Problemas visuales", medico2, consultorio2, fecha2, None,tipoCita.OPTOMETRIA) 
    cita7 = Cita(7,None, "Revisión visual", medico2, consultorio2, fecha4,None, tipoCita.OPTOMETRIA) 
    cita8 = Cita(8,Paciente1, "Problemas visuales", medico2, consultorio2, fecha5,None, tipoCita.OPTOMETRIA)
    cita8.setPago(Pago(None,15000))
		  
    cita12 = Cita(12,Paciente2, "Revisión visual", medico3, consultorio3,  fecha8,None, tipoCita.OPTOMETRIA) 
    cita13 = Cita(13,None, "Problemas visuales", medico3, consultorio3, fecha9,None, tipoCita.OPTOMETRIA)
    cita17 = Cita(17,Paciente3, "Revisión visual", medico3, consultorio3, fecha10,None, tipoCita.OPTOMETRIA) 
    cita18 = Cita(18,None, "Problemas visuales", medico3, consultorio3, fecha5,None, tipoCita.OPTOMETRIA)
    cita12.setPago(Pago(None, 15000))
    cita17.setPago(Pago(None,15000))
		  	  
    cita4 = Cita(4, None, "Problemas en los oídos", medico4, consultorio4, fecha2, None,tipoCita.AUDIOMETRIA) 
    cita5 = Cita(5,None, "No escucha", medico4, consultorio4, fecha3,None, tipoCita.AUDIOMETRIA) 
    cita9 = Cita(9,None, "Problemas en los oídos", medico4, None, fecha6, None,tipoCita.AUDIOMETRIA) 
    cita10 = Cita(10,None, "No escucha", medico4,  consultorio4, fecha7, None,tipoCita.AUDIOMETRIA) 
    cita14 = Cita(14,None,  "Problemas en los oídos", medico4, None, fecha11,None, tipoCita.AUDIOMETRIA)
    cita15 = Cita(15,Paciente1, "No escucha", medico4, consultorio4, fecha12, None,tipoCita.AUDIOMETRIA) 
    cita19 = Cita(19,None, "Problemas en los oídos", medico4, None, fecha13, None,tipoCita.AUDIOMETRIA) 
    cita20 = Cita(20,Paciente3, "No escucha", medico4, consultorio4, fecha14, None,tipoCita.AUDIOMETRIA)
    cita15.setPago(Pago(None,15000))
    cita20.setPago(Pago(None,15000))
    
    entrega1 = Entrega(None,Paciente1, "calle 36 #89 53", None, estadoEntrega.EN_CAMINO);
    entrega2 = Entrega(None,Paciente1, "calle 36 #89 53", None, estadoEntrega.EN_CAMINO) 
    entrega3 = Entrega(None,Paciente2, "Carrera 68 # 54 12", None, estadoEntrega.EN_CAMINO)
    entrega4 = Entrega(None,Paciente3, "cra87#12-34", None, estadoEntrega.EN_CAMINO)
		  
    entrega1.setPago(Pago(None,10000))
    entrega2.setPago(Pago(None,10000))
    entrega3.setPago(Pago(None,10000))
    entrega4.setPago(Pago(None,10000))
		  
    Paciente1.getEntregas().update({fecha10 : entrega1})
    Paciente1.getEntregas().update({fecha11 : entrega2})
    Paciente2.getEntregas().update({fecha13: entrega3})
    Paciente3.getEntregas().update({fecha14 : entrega4})
    
    medicamento1 = Medicamentos(tipoMedicamento.ACETAMINOFEN, Paciente1, 2, 3)
    medicamento2 = Medicamentos(tipoMedicamento.IBUPROFENO, Paciente1, 4, 6)
    medicamento3 = Medicamentos(tipoMedicamento.AMOXICILINA, Paciente1, 1, 8)
    
    diagnostico = Diagnostico(Paciente1, "Dolor de cabeza", medicamento1, 1, cita1)
    diagnostico1 = Diagnostico(Paciente2, "Dolor de cabeza", medicamento2, 2, cita11)
    diagnostico2 = Diagnostico(Paciente3, "Rodilla Rota", medicamento3, 3, cita6) 
    
    diagnosticos1 = [diagnostico]
    diagnosticos2 = [diagnostico1]
    diagnosticos3 = [diagnostico2]
    
    historiaClinica1 = HistoriaClinica(Paciente1, diagnosticos1)
    historiaClinica2 = HistoriaClinica(Paciente2, diagnosticos2)
    historiaClinica3 = HistoriaClinica(Paciente3, diagnosticos3)
    diagnostico.setPersona(Paciente1)
    Paciente1.setHistoriaClinica(historiaClinica1)
    diagnostico1.setPersona(Paciente2)
    Paciente2.setHistoriaClinica(historiaClinica2)
    diagnostico2.setPersona(Paciente3)
    Paciente3.setHistoriaClinica(historiaClinica3)
    
    medico1.getConsultas().update({fecha1 : cita1})
    medico1.getConsultas().update({fecha2: None})
    medico1.getConsultas().update({fecha3: None})
    medico1.getConsultas().update({fecha4: cita6}) 
    medico1.getConsultas().update({fecha5: cita11}) 
    medico1.getConsultas().update({fecha6: cita16})
    medico1.getConsultas().update({fecha7: None}) 
    medico1.getConsultas().update({fecha8: None}) 
    medico1.getConsultas().update({fecha9: None})
    medico1.getConsultas().update({fecha10: None})
    medico1.getConsultas().update({fecha11: None})
    medico1.getConsultas().update({fecha12: None})
    medico1.getConsultas().update({fecha13: None})
    medico1.getConsultas().update({fecha14: None})
    
    medico2.getConsultas().update({fecha1: cita2})
    medico2.getConsultas().update({fecha2: cita3}) 
    medico2.getConsultas().update({fecha3: None})
    medico2.getConsultas().update({fecha4: cita7}) 
    medico2.getConsultas().update({fecha5: cita8}) 
    medico2.getConsultas().update({fecha6: None})
    medico2.getConsultas().update({fecha7: None})
    medico2.getConsultas().update({fecha8: None}) 
    medico2.getConsultas().update({fecha9: None})
    medico2.getConsultas().update({fecha10: None})
    medico2.getConsultas().update({fecha11: None})
    medico2.getConsultas().update({fecha12: None})
    medico2.getConsultas().update({fecha13: None})
    medico2.getConsultas().update({fecha14: None})
    
    medico3.getConsultas().update({fecha1: None}) 
    medico3.getConsultas().update({fecha2: None})
    medico3.getConsultas().update({fecha3: None})
    medico3.getConsultas().update({fecha4: None})
    medico3.getConsultas().update({fecha5: cita18})
    medico3.getConsultas().update({fecha6: None})
    medico3.getConsultas().update({fecha7: None}) 
    medico3.getConsultas().update({fecha8: cita12}) 
    medico3.getConsultas().update({fecha9: cita13})
    medico3.getConsultas().update({fecha10: cita17})
    medico3.getConsultas().update({fecha11: None})
    medico3.getConsultas().update({fecha12: None})
    medico3.getConsultas().update({fecha13: None})
    medico3.getConsultas().update({fecha14: None})
    
    medico4.getConsultas().update({fecha1: None})
    medico4.getConsultas().update({fecha2: cita4}) 
    medico4.getConsultas().update({fecha3: cita5})
    medico4.getConsultas().update({fecha4: None}) 
    medico4.getConsultas().update({fecha5: None}) 
    medico4.getConsultas().update({fecha6: cita9})
    medico4.getConsultas().update({fecha7: cita10})
    medico4.getConsultas().update({fecha8: None})
    medico4.getConsultas().update({fecha9: None})
    medico4.getConsultas().update({fecha10: None})
    medico4.getConsultas().update({fecha11: cita14})
    medico4.getConsultas().update({fecha12: cita15})
    medico4.getConsultas().update({fecha13: cita19})
    medico4.getConsultas().update({fecha14: cita20})
    
    consultorio1.getConsultas().update({fecha1: cita1})
    consultorio1.getConsultas().update({fecha2: None})
    consultorio1.getConsultas().update({fecha3: None})
    consultorio1.getConsultas().update({fecha4: cita6})
    consultorio1.getConsultas().update({fecha5: cita11})
    consultorio1.getConsultas().update({fecha6: cita16})
    consultorio1.getConsultas().update({fecha7: None})
    consultorio1.getConsultas().update({fecha8: None})
    consultorio1.getConsultas().update({fecha9: None})
    consultorio1.getConsultas().update({fecha10: None})
    consultorio1.getConsultas().update({fecha11: None})
    consultorio1.getConsultas().update({fecha12: None})
    consultorio1.getConsultas().update({fecha13: None})
    consultorio1.getConsultas().update({fecha14: None})
		  
    consultorio2.getConsultas().update({fecha1: cita2})
    consultorio2.getConsultas().update({fecha2: cita3})
    consultorio2.getConsultas().update({fecha3: None})
    consultorio2.getConsultas().update({fecha4: cita7})
    consultorio2.getConsultas().update({fecha5: cita8})
    consultorio2.getConsultas().update({fecha6: None})
    consultorio2.getConsultas().update({fecha7: None})
    consultorio2.getConsultas().update({fecha8: None})
    consultorio2.getConsultas().update({fecha9: None})
    consultorio2.getConsultas().update({fecha10: None})
    consultorio2.getConsultas().update({fecha11: None})
    consultorio2.getConsultas().update({fecha12: None})
    consultorio2.getConsultas().update({fecha13: None})
    consultorio2.getConsultas().update({fecha14: None})
		  
    consultorio3.getConsultas().update({fecha1: None})
    consultorio3.getConsultas().update({fecha2: None})
    consultorio3.getConsultas().update({fecha3: None})
    consultorio3.getConsultas().update({fecha4: None})
    consultorio3.getConsultas().update({fecha5: cita18})
    consultorio3.getConsultas().update({fecha6: None})
    consultorio3.getConsultas().update({fecha7: None})
    consultorio3.getConsultas().update({fecha8: cita12})
    consultorio3.getConsultas().update({fecha9: cita13})
    consultorio3.getConsultas().update({fecha10: cita17})
    consultorio3.getConsultas().update({fecha11: None})
    consultorio3.getConsultas().update({fecha12: None})
    consultorio3.getConsultas().update({fecha13: None})
    consultorio3.getConsultas().update({fecha14: None})
		  
    consultorio4.getConsultas().update({fecha1: None})
    consultorio4.getConsultas().update({fecha2: cita4})
    consultorio4.getConsultas().update({fecha3: cita5})
    consultorio4.getConsultas().update({fecha4: None})
    consultorio4.getConsultas().update({fecha5: None})
    consultorio4.getConsultas().update({fecha6: cita9})
    consultorio4.getConsultas().update({fecha7: cita10})
    consultorio4.getConsultas().update({fecha8: None})
    consultorio4.getConsultas().update({fecha9: None})
    consultorio4.getConsultas().update({fecha10: None})
    consultorio4.getConsultas().update({fecha11: cita14})
    consultorio4.getConsultas().update({fecha12: cita15})
    consultorio4.getConsultas().update({fecha13: cita19})
    consultorio4.getConsultas().update({fecha14: cita20})
		  
    Paciente1.getConsultas().update({fecha1: cita1})
    Paciente1.getConsultas().update({fecha5: cita8})
    Paciente1.getConsultas().update({fecha12: cita15})
		  
    Paciente2.getConsultas().update({fecha5: cita11})
    Paciente2.getConsultas().update({fecha8: cita12})
		  
    Paciente3.getConsultas().update({fecha4: cita6})
    Paciente3.getConsultas().update({fecha10: cita17})
    Paciente3.getConsultas().update({fecha14: cita20})
    
    Administrador.getFechas().append(fecha1)
    Administrador.getFechas().append(fecha2)
    Administrador.getFechas().append(fecha3)
    Administrador.getFechas().append(fecha4)
    Administrador.getFechas().append(fecha5)
    Administrador.getFechas().append(fecha6)
    Administrador.getFechas().append(fecha7)
    Administrador.getFechas().append(fecha8)
    Administrador.getFechas().append(fecha9)
    Administrador.getFechas().append(fecha10)
    Administrador.getFechas().append(fecha11)
    Administrador.getFechas().append(fecha12)
    Administrador.getFechas().append(fecha13)
    Administrador.getFechas().append(fecha14)
    Administrador.setDinero(500000)
    
    serializar()
    """
    imagenes = ["Imagenes/inicio/1.jpg", "Imagenes/inicio/2.jpg", "Imagenes/inicio/3.jpg", "Imagenes/inicio/4.jpg", "Imagenes/inicio/5.jpg"]
    andres = ["Imagenes/Andres/1.jpg", "Imagenes/Andres/2.jpg", "Imagenes/Andres/3.jpg", "Imagenes/Andres/4.jpg"]
    luzarait = ["Imagenes/Luzarait/1.jpg", "Imagenes/Luzarait/2.jpg", "Imagenes/Luzarait/3.jpg", "Imagenes/Luzarait/4.jpg"]
    natalia = ["Imagenes/Natalia/1.jpg", "Imagenes/Natalia/2.jpg", "Imagenes/Natalia/3.jpg", "Imagenes/Natalia/4.jpg"]
    roger = ["Imagenes/Roger/1.jpg", "Imagenes/Roger/2.jpg", "Imagenes/Roger/3.jpg", "Imagenes/Roger/4.jpg"]
    yeferson = ["Imagenes/Yeferson/1.jpg", "Imagenes/Yeferson/2.jpg", "Imagenes/Yeferson/3.jpg", "Imagenes/Yeferson/4.jpg"]
    dir = imagenes + andres + luzarait + natalia + roger + yeferson
    try:
        ExcepcionPresenciaArchivos.presenciaArchivos(["baseDatos/temp/administrador", "baseDatos/temp/consultas", 
        "baseDatos/temp/consultorios","baseDatos/temp/diagnosticos", "baseDatos/temp/fechas", 
        "baseDatos/temp/historiasClinicas", "baseDatos/temp/listaSintomas", "baseDatos/temp/medicamentos",
        "baseDatos/temp/medicos", "baseDatos/temp/pacientes"])
        ExcepcionPresenciaImagenes.presenciaImagenes(dir)
        deserializar()
    except ExcepcionPresenciaArchivos:
        return
    except ExcepcionPresenciaImagenes:
        return


inicializar()

ventana = tk.Tk()
ventana.title('Sistema gestor médico')
ventana.geometry("+10+10")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventanaExamenes = solicitarExamen()
ventanaExamenes.pack_forget()
ventanaSolicitarCitas = solicitarCita()
ventanaSolicitarCitas.pack_forget()
ventanaReagendarCitas = reagendarCita()
ventanaReagendarCitas.pack_forget()
ventanaMostrar = mostrarDiagnostico()
ventanaMostrar.pack_forget()
ventanaSolicitar = solicitarEntregaMedicamentos()
ventanaSolicitar.pack_forget()
ventanaCrear = crearDiagnostico()
ventanaCrear.pack_forget()
ventanaPagarConsulta = pagarConsulta()
ventanaPagarConsulta.pack_forget()
ventanaPagarEntrega = pagarEntrega()
ventanaPagarEntrega.pack_forget()

posicionImagen=1
def cambiarImagen(e):
    global posicionImagen
    posicionImagen += 1
    if posicionImagen == 6:
        posicionImagen = 1
    FotoInicio=(Image.open("Imagenes/inicio/" + str(posicionImagen) + ".jpg")).resize((400,400), Image.ANTIALIAS)
    FotoInicio = ImageTk.PhotoImage(FotoInicio)
    LabelFotoInicio.configure(image=FotoInicio)
    LabelFotoInicio.image=FotoInicio

# Poner aquí las biografías
VidaAndres = ""
VidaLuzarait = ""
VidaNatalia = ""
VidaRoger = ""
VidaYeferson = ""

posicionVida=0
def cambiarVida(e):
    global posicionVida
    posicionVida += 1
    if posicionVida == 5:
        posicionVida = 0
    ListaFotos=["Andres", "Luzarait", "Natalia", "Roger", "Yeferson"]
    Foto1 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/1.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto1 = ImageTk.PhotoImage(Foto1)
    Foto2 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/2.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto2 = ImageTk.PhotoImage(Foto2)
    Foto3 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/3.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto3 = ImageTk.PhotoImage(Foto3)
    Foto4 =(Image.open("Imagenes/" + ListaFotos[posicionVida] + "/4.jpg")).resize((200,200), Image.ANTIALIAS)
    Foto4 = ImageTk.PhotoImage(Foto4)
    LabelFoto1.configure(image=Foto1)
    LabelFoto1.image=Foto1
    LabelFoto2.configure(image=Foto2)
    LabelFoto2.image=Foto2
    LabelFoto3.configure(image=Foto3)
    LabelFoto3.image=Foto3
    LabelFoto4.configure(image=Foto4)
    LabelFoto4.image=Foto4
    if posicionVida==0:
        CuerpoVida.config(text=VidaAndres)
    elif posicionVida==1:
        CuerpoVida.config(text=VidaLuzarait)
    elif posicionVida==2:
        CuerpoVida.config(text=VidaNatalia)
    elif posicionVida==3:
        CuerpoVida.config(text=VidaRoger)
    elif posicionVida==4:
        CuerpoVida.config(text=VidaYeferson)

def descripcion():
    descripcion = """En el sistema gestor médico los pacientes podrán solicitar citas o exámenes y reagendar sus citas; también podrán pagar sus consultas, solicitar la entrega de medicamentos y realizar el pago de estas.
Por otro lado, los médicos podrán crear diagnósticos que añadir a la historia clínica de un paciente.
Por último, el administrador podrá visualizar información referente a las consultas, exámenes y entregas realizadas; además, podrá contratar nuevos médicos, adquirir nuevos consultorios o comprar medicamentos."""
    messagebox.showinfo(title="Descripción de la aplicación",
                        message=descripcion)

def ocultarTodo():
    ventanaInicio.pack_forget()
    ventanaUsuario.pack_forget()
    ventanaExamenes.pack_forget()
    ventanaReagendarCitas.pack_forget()
    ventanaSolicitarCitas.pack_forget()
    ventanaMostrar.pack_forget()
    ventanaSolicitar.pack_forget()
    ventanaCrear.pack_forget()
    ventanaPagarConsulta.pack_forget()
    ventanaPagarEntrega.pack_forget()
    
def borrarTodo():
    ventanaExamenes.borrar()
    ventanaSolicitarCitas.borrar()
    
def ingresar():
    ocultarTodo()
    borrarTodo()
    ventanaUsuario.pack()
    ventana["menu"] = menuVentanaUsuario    
    
def evento():
    pass

def salir():
    finalizar = messagebox.askyesno(title="Salir",
                                message="¿Confirma que desea salir de la aplicación?",
                                detail="Clic en Sí para salir")
    if finalizar:
        serializar()
        ventana.destroy()
        serializar()
 
def salirUsuario():
    salir = messagebox.askyesno(title="Salir",
                                message="¿Confirma que desea regresar a la ventana de inicio?",
                                detail="Clic en Sí para regresar")
    if salir:
        ocultarTodo()
        ventanaInicio.pack()
        ventana["menu"] = menuVentanaInicio
        
def aplicacion():
    descripcion = """En el sistema gestor médico los pacientes podrán solicitar citas o exámenes y reagendar sus citas; también podrán pagar sus consultas, solicitar la entrega de medicamentos y realizar el pago de estas.
Por otro lado, los médicos podrán crear diagnósticos que añadir a la historia clínica de un paciente.
Por último, el administrador podrá visualizar información referente a las consultas, exámenes y entregas realizadas; además, podrá contratar nuevos médicos, adquirir nuevos consultorios o comprar medicamentos."""
    messagebox.showinfo(title="Información básica de la aplicación",
                        message=descripcion)
    
def acerca():
    autores = """Autores:
- Andrés Alexis Galvis Herrera
- Natalia Andrea Alvarez Hoyos
- Yeferson Steven Aguilar Alvarado
- Roger Vera Londoño
- Luzarait Cañas Quintero
"""
    messagebox.showinfo(title="Acerca de la aplicación",
                        message=autores) 
def solicitarExamen():
    ocultarTodo()
    borrarTodo()
    ventanaExamenes.pack()

def solicitarCita():
    ocultarTodo()
    borrarTodo()
    ventanaSolicitarCitas.pack()

def reagendarCita():
    ocultarTodo()
    ventanaReagendarCitas.pack()
def mostrarDiagnostico():
    ocultarTodo()
    ventanaMostrar.pack()

def solicitarEntregaMedicamentos():
    ocultarTodo()
    ventanaSolicitar.pack()

def crearDiagnostico():
    ocultarTodo()
    ventanaCrear.pack()

def pagarConsulta():
    ocultarTodo()
    ventanaPagarConsulta.pack()

def pagarEntrega():
    ocultarTodo()
    ventanaPagarEntrega.pack()

# Solicitar examen



 
 
   
# Menú ventana de inicio
menuVentanaInicio = Menu(ventana, font="Helvetica 11 bold", fg="red")
menuInicio = Menu(menuVentanaInicio, font="Helvetica 11",)
menuVentanaInicio.add_cascade(menu=menuInicio, label="Inicio")
menuInicio.add_command(label="Descripción", command= descripcion)
menuInicio.add_command(label="Salir", command= salir)
ventana["menu"] = menuVentanaInicio

# Se crean cada uno de los frames especificados para la ventana de Inicio.
ventanaInicio = Frame()
P1 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P2 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P3 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P4 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P5 = Frame(master=P2, highlightbackground="black", highlightthickness=2)
P6 = Frame(master=P2, highlightbackground="black", highlightthickness=2)

# Se crea el Label de bienvenida a la aplicación.
Saludo = Label(master=P3, text="""Bienvenido al sistema gestor médico, que lo ayudará 
a administrar facilmente todo lo que tiene que ver con este.""", font="Helvetica 11")

# Se crea el botón "Ingresar", que al ser presionado permitirá al usuario acceder a las funcionalidades.
Ingreso = Button(master=P4, text="Ingresar", font="Helvetica 11 bold", 
                bg="grey", fg="white", borderwidth=5, relief="groove",
                command=ingresar)

# Se crea el título para las hojas de vida de los autores.
TituloVida = Label(master=P5, text="Breve biografía de los autores", 
                font="Helvetica 11 bold")

# Se crea el Label para el texto de las hojas de vida de los autores.
CuerpoVida = Label(master=P5, text="Aquí va la hoja de vida", font="Helvetica 10", 
                anchor=W)

# Se crea el Label que contendrá las instrucciones para cambiar entre hojas de vida de los autores.
PieVida = Label(master=P5, text="Clic sobre la biografía para cambiar de autor",
                font="Helvetica 8 italic", fg="blue")

# Se localizan las imágenes iniciales para las relacionadas con la aplicación y para las de hojas de vida de los autores.
FotoInicio=(Image.open("Imagenes/inicio/1.jpg")).resize((400,400), Image.LANCZOS)
FotoInicio = ImageTk.PhotoImage(FotoInicio)
Foto1 =(Image.open("Imagenes/Andres/1.jpg")).resize((200,200), Image.LANCZOS)
Foto1 = ImageTk.PhotoImage(Foto1)
Foto2 =(Image.open("Imagenes/Andres/2.jpg")).resize((200,200), Image.LANCZOS)
Foto2 = ImageTk.PhotoImage(Foto2)
Foto3 =(Image.open("Imagenes/Andres/3.jpg")).resize((200,200), Image.LANCZOS)
Foto3 = ImageTk.PhotoImage(Foto3)
Foto4 =(Image.open("Imagenes/Andres/4.jpg")).resize((200,200), Image.LANCZOS)
Foto4 = ImageTk.PhotoImage(Foto4)

# Se crean los Label para las imágenes relacionadas con la aplicación y para las de hojas de vida de los autores.
LabelFotoInicio = Label(master=P4, image=FotoInicio, borderwidth=5, relief="ridge")
LabelFoto1 = Label(master=P6, image=Foto1, borderwidth=5, relief="ridge")
LabelFoto1.grid(column=0, row=0, padx=3, pady=3)
LabelFoto2 = Label(master=P6, image=Foto2, borderwidth=5, relief="ridge")
LabelFoto2.grid(column=1, row=0, padx=3, pady=3)
LabelFoto3 = Label(master=P6, image=Foto3, borderwidth=5, relief="ridge")
LabelFoto3.grid(column=0, row=1, padx=3, pady=3)
LabelFoto4 = Label(master=P6, image=Foto4, borderwidth=5, relief="ridge")
LabelFoto4.grid(column=1, row=1, padx=3, pady=3)

# Se visualizan todos los elementos anteriormente creados.
ventanaInicio.pack()
P1.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
P2.pack(side=RIGHT, fill=BOTH, padx=5, pady=5)
P3.pack(side=TOP, fill=BOTH, padx=5, pady=5)
P4.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
P5.pack(side=TOP, fill=BOTH, padx=5, pady=5)
P6.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
Saludo.pack(padx=5, pady=5)
Ingreso.pack(side=BOTTOM, padx=5, pady=5)
LabelFotoInicio.pack(side=TOP, padx=10, pady=10)
TituloVida.pack(padx=5, pady=5)
CuerpoVida.pack(padx=5, pady=5)
PieVida.pack(padx=5, pady=5)

# Se asignan los comandos para cambiar de hoja de vida y de imagen relacionada a la aplicación.
CuerpoVida.bind("<Button-1>", cambiarVida)
LabelFotoInicio.bind("<Enter>", cambiarImagen)  

# Menú de la ventana de usuario
menuVentanaUsuario = Menu(ventana, font="Helvetica 11 bold")

menuArchivo = Menu(menuVentanaUsuario, font="Helvetica 11")
menuVentanaUsuario.add_cascade(menu=menuArchivo, label="Archivo")
menuArchivo.add_command(label="Aplicación", command=aplicacion)
menuArchivo.add_command(label="Salir", command=salirUsuario)


menuProcesos = Menu(menuVentanaUsuario, font="Helvetica 11")
menuVentanaUsuario.add_cascade(label="Procesos y consultas", menu=menuProcesos)

menuCitas = Menu(menuProcesos, font="Helvetica 11")
menuProcesos.add_cascade(label="Citas", menu= menuCitas)
menuCitas.add_command(label="Solicitar cita", command=solicitarCita)
menuCitas.add_command(label="Reagendar cita", command=reagendarCita)

menuProcesos.add_command(label="Exámenes", command=solicitarExamen)

menuFinanzas = Menu(menuProcesos, font="Helvetica 11")
menuProcesos.add_cascade(label="Finanzas", menu= menuFinanzas)
menuFinanzas.add_command(label="Pagar consultas", command=pagarConsulta)
menuFinanzas.add_command(label="Pagar entregas", command=pagarEntrega)
menuFinanzas.add_command(label="Consultar dinero disponible", command=evento)
menuFinanzas.add_command(label="Pago de nómina", command=evento)

menuResultadosMedicamentos = Menu(menuProcesos, font="Helvetica 11")
menuProcesos.add_cascade(label="Resultados y Medicamentos", menu= menuResultadosMedicamentos)
menuResultadosMedicamentos.add_command(label="Crear diagnóstico", command=crearDiagnostico)
menuResultadosMedicamentos.add_command(label="Mostrar diagnósticos", command=mostrarDiagnostico)
menuResultadosMedicamentos.add_command(label="Solicitar entrega medicamentos", command=solicitarEntregaMedicamentos)

menuAdministracion = Menu(menuProcesos, font="Helvetica 11")
menuProcesos.add_cascade(label="Administración", menu= menuAdministracion)
menuAdministracion.add_command(label="Visualizar citas, exámenes y entregas", command=evento)
menuAdministracion.add_command(label="Contratar médicos", command=evento)
menuAdministracion.add_command(label="Adquirir consultorios", command=evento)
menuAdministracion.add_command(label="Comprar medicamentos", command=evento)


menuAyuda = Menu(menuVentanaUsuario, font="Helvetica 11")
menuVentanaUsuario.add_cascade(menu=menuAyuda, label="Ayuda")
menuAyuda.add_command(label="Acerca de", command=acerca)

# Se define el mensaje que aparecerá cuando se accede a la ventana de Usuario desde la ventana de Inicio.
tutorial = """           (0 0)           
          ---oOO-- (_) ----oOO---        
    ╔════════════════════════════════════════╗  
    ║ Bienveniedo al Sistema Medico! ♥       ║  
    ╚════════════════════════════════════════╝  
        --------------       
       |__|__|     
     || ||   
    ooO Ooo"
    explicacion del programa sobre el sistema medico
    ...
    ...
    ...
    
"""    

# Se crea la ventana de usuario, así como la sección de qué se puede hacer con la aplicación.
ventanaUsuario = Frame()
tituloInfo = Label(master=ventanaUsuario, text="¿Cómo usar esta aplicación y qué puede hacer con ella?", font="Helvetica 11 bold")
info = Label(master=ventanaUsuario, text=tutorial, font="Helvetica 10")
tituloInfo.pack(fill=BOTH, padx=5, pady=5)
info.pack(fill=BOTH, padx=5, pady=5)



ventana.mainloop()