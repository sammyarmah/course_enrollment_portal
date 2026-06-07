import pytest

# enrolling a student
@pytest.mark.asyncio
async def test_student_enrolls(
    client,
    student_token,
    admin_token
):

    course = await client.post(
        "/api/v1/courses",
        headers={
            "Authorization":
            f"Bearer {admin_token}"
        },
        json={
            "title":"SQLAlchemy",
            "code":"SQL101",
            "capacity":10
        }
    )

    course_id = course.json()["id"]

    response = await client.post(
        "/api/v1/enrollments",
        headers={
            "Authorization":
            f"Bearer {student_token}"
        },
        json={
            "course_id": course_id
        }
    )

    assert response.status_code == 201
    
    
# preventing duplicate enrollment
@pytest.mark.asyncio
async def test_duplicate_enrollment(
    client,
    student_token,
    admin_token
):

    course = await client.post(
        "/api/v1/courses",
        headers={
            "Authorization":
            f"Bearer {admin_token}"
        },
        json={
            "title":"Docker",
            "code":"DOC101",
            "capacity":10
        }
    )

    course_id = course.json()["id"]

    await client.post(
        "/api/v1/enrollments",
        headers={
            "Authorization":
            f"Bearer {student_token}"
        },
        json={
            "course_id": course_id
        }
    )

    response = await client.post(
        "/api/v1/enrollments",
        headers={
            "Authorization":
            f"Bearer {student_token}"
        },
        json={
            "course_id": course_id
        }
    )

    assert response.status_code == 400