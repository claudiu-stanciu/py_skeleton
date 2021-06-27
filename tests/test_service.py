import pytest


@pytest.mark.asyncio
async def test_service_compute_expect_return_true(service):
    actual_compute_res = await service.compute()
    expected_compute_res = True
    assert actual_compute_res == expected_compute_res
