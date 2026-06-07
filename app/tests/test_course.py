import pytest


@pytest.mark.asyncio
async def test_get_courses(
    client
):

    response = await client.get(
        "/api/v1/courses"
    )

    assert response.status_code == 200
    
# admin creating a course
@pytest.mark.asyncio
async def test_create_course(
    client,
    admin_token
):

    response = await client.post(
        "/api/v1/courses",
        headers={
            "Authorization":
            f"Bearer {admin_token}"
        },
        json={
            "title":"FastAPI",
            "code":"FAST101",
            "capacity":50
        }
    )

    assert response.status_code == 201
    
# student cannot create a course
@pytest.mark.asyncio
async def test_student_cannot_create_course(
    client,
    student_token
):

    response = await client.post(
        "/api/v1/courses",
        headers={
            "Authorization":
            f"Bearer {student_token}"
        },
        json={
            "title":"Python",
            "code":"PY101",
            "capacity":20
        }
    )

    assert response.status_code == 403