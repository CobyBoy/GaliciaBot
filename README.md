
Instalar [Python](https://www.python.org/downloads/)
Instalar [pip](https://pip.pypa.io/en/stable/installing/]) si no se instaló
Instalar Selenium
```
pip install selenium
```

#TOKEN y CHAT_ID
Crear bot en telegram con [BotFather](https://t.me/BotFather) o buscarlo desde la app de Telegram
para obtener el TOKEN seguir las instruccciones
para obtener el CHAT_ID propio: buscar @userinfobot en tg e iniciar el bot

Reemplazar lo obtenido en el archivo credentials.py

En el archivo constants.py: 
TRANSFERENCIA_A_BUSCAR debe reemplazarse con el movimiento que se desea buscar (devuelve el más reciente).
Ej: para recibir mensaje de telegram si Accenture pagó el sueldo sería: SIST. NAC. DE PAGOS -  HABERES

En el archivo run.py, la función:
```
isPenultimateWorkingDayOfTheMonth()
```

eliminar el 
```
-1
```
si se cobra el ultimo día hábil del mes.

Si no es el día de cobro, el script no corre. Para probar se puede reemplazar la función anteriormente mencionada con 
```
if(True)
// runs script
```