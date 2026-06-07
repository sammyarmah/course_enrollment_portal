import pytest


@pytest.mark.asyncio
async def test_get_profile(
    client,
    student_token
):

    response = await client.get(
        "/api/v1/users/me",
        headers={
            "Authorization":
            f"Bearer {student_token}"
        }
    )

    assert response.status_code == 200