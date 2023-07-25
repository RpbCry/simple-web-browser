import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.setCentralWidget(self.browser)

        # Create navigation bar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        # Add navigation buttons
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        nav_bar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        nav_bar.addAction(home_btn)

        # Add URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        # Add status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
