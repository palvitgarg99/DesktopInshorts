from main import check_api

api_url = "https://inshortsv2.vercel.app/news?type="


def test_get_api():
    response = check_api()
    assert response == 200
