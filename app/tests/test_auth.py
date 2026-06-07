import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_register_user(
    client
):

    response = await client.post(
        "/api/v1/auth/register",
        json={
            "name": "John Doe",
            "email": "john@test.com",
            "password": "password123",
            "role": "student"
        }
    )

    assert response.status_code == 201
    
# login test
import pytest


@pytest.mark.asyncio
async def test_login_user(
    client
):

    await client.post(
        "/api/v1/auth/register",
        json={
            "name": "Jane",
            "email": "jane@test.com",
            "password": "password123",
            "role": "student"
        }
    )

    response = await client.post(
        "/api/v1/auth/login",
        json={
            "email": "jane@test.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body
    
@pytest_asyncio.fixture
async def student_token(client):

    await client.post(
        "/api/v1/auth/register",
        json={
            "name":"Student",
            "email":"student@test.com",
            "password":"password123",
            "role":"student"
        }
    )

    response = await client.post(
        "/api/v1/auth/login",
        json={
            "email":"student@test.com",
            "password":"password123"
        }
    )

    return response.json()["access_token"]


@pytest_asyncio.fixture
async def admin_token(client):

    await client.post(
        "/api/v1/auth/register",
        json={
            "name":"Admin",
            "email":"admin@test.com",
            "password":"password123",
            "role":"admin"
        }
    )

    response = await client.post(
        "/api/v1/auth/login",
        json={
            "email":"admin@test.com",
            "password":"password123"
        }
    )

    return response.json()["access_token"]