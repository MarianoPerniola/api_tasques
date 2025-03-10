from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TODO: els vostres test venen aqui


# Test de `update_tasks`
def test_update_tasks(mocker):
    # Mockeamos la sesión de la base de datos
    mock_db = MagicMock()

    # Simulamos una tarea ya existente
    existing_task = Task(id=1, title="Tarea existente", description="Descripción existente")
    mock_db.query.return_value.filter.return_value.first.return_value = existing_task

    # Creamos un objeto TaskUpdate con los nuevos datos
    task_update = TaskUpdate(title="Tarea actualizada", description="Descripción actualizada")

    # Simulamos el comportamiento de la actualización
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = existing_task

    # Llamamos a la función `update_tasks`
    updated_task = update_tasks(mock_db, 1, task_update)

    # Comprobamos que los datos de la tarea se han actualizado correctamente
    assert updated_task.title == "Tarea actualizada"
    assert updated_task.description == "Descripción actualizada"


# Test de `delete_tasks`
def test_delete_tasks(mocker):
    # Mockeamos la sesión de la base de datos
    mock_db = MagicMock()

    # Simulamos una tarea existente
    existing_task = Task(id=1, title="Tarea a eliminar", description="Descripción de la tarea")
    mock_db.query.return_value.filter.return_value.first.return_value = existing_task

    # Simulamos el comportamiento de la eliminación
    mock_db.commit.return_value = None

    # Llamamos a la función `delete_tasks`
    deleted_task = delete_tasks(mock_db, 1)

    # Comprobamos que la tarea ha sido eliminada
    assert deleted_task.id == 1
    assert deleted_task.title == "Tarea a eliminar"
    mock_db.delete.assert_called_once_with(existing_task)
