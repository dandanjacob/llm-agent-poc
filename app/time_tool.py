import requests

def get_time(location: str) -> str:
    location = location.strip()

    try:
        zones_resp = requests.get(
            "https://worldtimeapi.org/api/timezone",
            timeout=5
        )
        zones_resp.raise_for_status()

        zones = zones_resp.json()
        match = next(
            (z for z in zones if location.lower() in z.lower()),
            None
        )

        if match:
            time_resp = requests.get(
                f"https://worldtimeapi.org/api/timezone/{match}",
                timeout=5
            )
            time_resp.raise_for_status()

            data = time_resp.json()
            return data["datetime"]

    except requests.exceptions.RequestException:
        pass 

    try:
        fallback_resp = requests.get(
            f"https://timeapi.io/api/Time/current/zone?timeZone={location}",
            timeout=5
        )
        fallback_resp.raise_for_status()

        data = fallback_resp.json()
        return data["dateTime"]

    except requests.exceptions.RequestException:
        return "Time service is temporarily unavailable."
