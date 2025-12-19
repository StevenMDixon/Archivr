from view.base import GuiBase
from domain.actions import Actions

if __name__ == "__main__":
    app = GuiBase(Actions())
    app.run()