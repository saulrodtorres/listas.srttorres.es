



// Usada en listas/templates/listas/tarea.html
function borrar_tarea(url) {
    window.location.href = url;
}

// Usadas en listas/templates/listas/index.html
function editar_lista(url) {
    window.location.href = url;
}
function crear_lista(url) {
    window.location.href = url;
}

// tabla de listas
    $(document).ready( function () {
        $('#listas_de_tareas').DataTable();
    } );

// tabla de tareas
    $(document).ready( function () {
        $('#lista_de_tareas').DataTable();
    } );

    function borrar_lista() {
        // Code to delete the list with {{lista.id}}
        //alert("Se va a borrar la lista con id: {{lista.id}}")
        if (confirm('Seguro que desea borrar la lista con id: {{lista.id}}?')) {
        // Save it!
        console.log('La lista con id: {{lista.id}} ha sido borrada con éxito.');
        } else {
        // Do nothing!
        console.log('Has cancelado el borrado de la lista con id: {{lista.id}}.');
        }
        window.location.href ="{% url 'listas:borrar_lista' lista.id %}";
    }
    function editar_tarea(url) {
        window.location.href = url;
        }
    function borrar_tarea(url) {
        window.location.href = url;
        }
    function crear_tarea(url) {
        window.location.href = url;
        }