from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TODO: els vostres test venen aqui

def test_get_tasks(mocker):
    mock_db = MagicMock()
    
    mock_db.query.return_value.all.return_value = [
        Task(id=1, title="Tarea 1", description="Descripción 1"),
        Task(id=2, title="Tarea 2", description="Descripción 2")
    ]
    
    tasks = get_tasks(mock_db)
    
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[0].title == "Tarea 1"
    assert tasks[1].title == "Tarea 2"


def test_create_tasks(mocker):
    mock_db = MagicMock()

    task_data = TaskCreate(title="Nueva tarea", description="Descripción de la nueva tarea")
    
    mock_task = Task(id=1, **task_data.dict())
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = mock_task
    
    task = create_tasks(mock_db, task_data)
    
    assert task.id == 1
    assert task.title == "Nueva tarea"
    assert task.description == "Descripción de la nueva tarea"
