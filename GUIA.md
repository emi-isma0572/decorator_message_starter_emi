# Guía de la actividad Decorator

## 1. Preparar tu repositorio en Windows

Si ya lo tienes clonado, abre su carpeta en VS Code. Si no:

```powershell
git clone https://github.com/emi-isma0572/decorator_message_starter_emi.git
cd decorator_message_starter_emi
git switch -c feat/message-decorators
```

Si ya estás en esa rama, omite el último comando.

## 2. Agregar la solución

Copia desde esta solución los siguientes archivos a las mismas rutas en tu repositorio:

- src/messages/message_decorator.py
- src/messages/urgent_decorator.py
- src/messages/timestamp_decorator.py
- src/demo.py
- tests/test_message_decorators.py

No reemplaces PlainMessage: permanece exactamente igual. Tampoco se necesita cambiar Message, __init__.py ni el test original.

## 3. Entender cada clase

- Message es el componente abstracto: establece render().
- PlainMessage es el componente concreto: devuelve el texto original.
- MessageDecorator hereda de Message y guarda otro Message en self._message. Su render() delega al objeto envuelto. Combina herencia (es un Message) y composición (contiene un Message).
- UrgentDecorator hereda el constructor del decorador base. Su render() obtiene el contenido mediante super().render() y antepone [URGENT].
- TimestampDecorator recibe el mensaje y un timestamp de texto. super().__init__(message) guarda el mensaje en la clase base; su render() antepone el timestamp recibido.

super().render() llama al método de MessageDecorator, que a su vez llama a self._message.render(). Así se recorre la cadena sin preguntar el tipo concreto de cada objeto.

El timestamp se recibe por constructor: no se consulta el reloj del sistema. La prueba siempre obtiene el mismo resultado. Esta actividad no requiere implementar validación o formato de fechas.

## 4. Crear el entorno y ejecutar

Desde la raíz del repositorio:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe src/demo.py
```

Se usa directamente el Python del entorno para evitar depender de la activación de PowerShell.

La demo imprime:

```text
[2026-10-30 14:30:00] [URGENT] Deploy complete
[URGENT] [2026-10-30 14:30:00] Deploy complete
```

El test original verifica PlainMessage. El nuevo test se enfoca en la composición: ambas cadenas siguen siendo Message, los dos prefijos aparecen en el orden correcto y el mensaje original conserva su contenido.

## 5. Explicar el apilamiento

```python
message = TimestampDecorator(
    UrgentDecorator(PlainMessage("Deploy complete")),
    "2026-10-30 14:30:00",
)
print(message.render())
```

Se construye primero PlainMessage, luego UrgentDecorator lo envuelve y finalmente TimestampDecorator envuelve a UrgentDecorator. Para renderizar, la llamada entra por el decorador externo y llega hasta PlainMessage. Al regresar, se agrega primero URGENT y luego el timestamp.

El cliente solo usa render(): el contrato permanece estable aunque cambie la combinación de decoradores. Cada clase principal está en su propio archivo.

## 6. Respuestas para explicar en clase

¿Importa el orden? Sí, en esta implementación cambia el texto final. TimestampDecorator(UrgentDecorator(plain), timestamp) coloca primero la fecha; UrgentDecorator(TimestampDecorator(plain, timestamp)) coloca primero URGENT. Ambos comportamientos permanecen, pero su presentación cambia. En otros diseños el efecto puede ser mayor, por ejemplo si una capa transforma la salida de otra.

¿Qué costo de complejidad introduce? Hay más objetos y llamadas indirectas: para entender o depurar un resultado hay que seguir la cadena y su orden. Por cada decorador se agrega un objeto y una llamada delegada. La ventaja es poder combinar responsabilidades sin modificar PlainMessage ni crear una subclase para cada combinación.

## 7. Revisar y subir tu entrega

```powershell
git status
git diff
git add src/messages/message_decorator.py src/messages/urgent_decorator.py src/messages/timestamp_decorator.py src/demo.py tests/test_message_decorators.py
git commit -m "Implement message decorators with deterministic timestamp"
git push -u origin feat/message-decorators
```

Después abre en GitHub un pull request hacia main si tu profesor pide entregar mediante PR. Título sugerido: Implement message decorators. Descripción sugerida: Adds composable urgent and timestamp decorators while keeping PlainMessage unchanged. Includes a deterministic demo and a focused test for stacking order. Validation: python -m pytest -q.

Estos cambios se prepararon localmente: no se han publicado commits, ramas ni pull requests en GitHub desde esta conversación.
