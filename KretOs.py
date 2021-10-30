
#============= K r e t O s ==================

# Modificación de registros en KoboToolbox

# Desarrollado por: Gabriel Oliveros.
# GitHub: gabroliveros

#=============================================

import requests
import json

TOKEN = '' #Indica aquí tu Token de acceso a la API
PARAMS = {'format': 'json'}
HEADERS = {'Authorization': f'Token {TOKEN}'}


#Recuerda utilizar el servidor que te corresponde.
#Se utiliza acá, por defecto, humanitarianresponse.info 


def estatus(asset, submission_id, status):
    '''
    Cambia el estatus de un registro determinado en un formulario.

    asset: (string) código del formulario (ver "Kobo_URLs.txt").
    submission_id: (string) identificador del registro (se encuentra en Kobo como "_id").
    status: (string) estatus del registro. Opciones approved, not_approved, on_hold, (en blanco para sin estatus).
    '''
    
    URL= 'https://kobo.humanitarianresponse.info/api/v2/assets/'+asset+'/data/'+submission_id+'/validation_status/'
    res = requests.patch(url= URL,
                         data= {'validation_status.uid': 'validation_status_'+status},
                         params= PARAMS,
                         headers= HEADERS)


def cambiar(asset, submission_id, grupo_preg, valor_nuevo):
    '''
    Cambia o edita el valor de un ítem o pregunta específica.
    Los grupos con múltiples sub-registros no admiten modificación en Kobo por ahora.
    
    grupo_preg: (string) Identificador del grupo (si existe) en el formulario y de la pregunta. Van separados con "/"
        Si el grupo no existe se coloca solo el identificador de la pregunta. Ej: {'nombre_grupo/pregunta': 'nuevo valor'}}
        o {'pregunta': 'nuevo valor'}}
    valor_nuevo: (string) Valor que se desea introducir.
    '''

    URL = 'https://kobo.humanitarianresponse.info/api/v2/assets/'+asset+'/data/bulk/'
    payload = {'submission_ids': [submission_id],
               'data': {grupo_preg : valor_nuevo}}
    res = requests.patch(url= URL,
                         data= {'payload': json.dumps(payload)},
                         params= PARAMS,
                         headers= HEADERS)


print('Bienvenido, KretOS comenzará a editar sus datos en KOBO')

#Parámetros generales a indicar:
#===============================
asset= 'f3ugKLy68woZwLnxHaYXzk' #Este es el código del formulario que se va a modificar. Debe verse así.

submission_id= ['121534789'] #Listado de registros a modificar. Aquí se indican los IDs de cada registro (_id)


#Para cambiar el status:
#=======================
status= 'approved' #Aquí se indica el nuevo status que se va a registrar

for ids in submission_id:
    estatus(asset, ids, status)
    print('{} modificado'.format(ids))


#Para cambiar el contenido de un registro en un determinado campo:
#=================================================================
'''
grupo_preg= 'C_digo_Familiar' #Si la pregunta está dentro de un grupo se referencia así: 'Nuevos_benef/C_digo_Familiar'
valor_nuevo= '' #Aquí se indica el nuevo valor que tendrá el campo

count= 0
for ids in submission_id:
    cambiar(asset, ids, grupo_preg, valor_nuevo)
    print('{} modificado {}'.format(ids,cod))
    count+=1
'''

print('\n','Trabajo finalizado con éxito.')
