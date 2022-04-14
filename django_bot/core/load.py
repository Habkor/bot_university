from django_bot.core.packages import PackagesLoader


def load_modules():
    """Основная функция для загрузки модулей."""
    PackagesLoader().load_packages(
        f"django_bot.app_bot.modules.{item}"
        for item in [
            "common",
            "decans",
            "students",
        ]
    )
