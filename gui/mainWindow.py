import sys
import os
from gui.modules import *
from gui.widgets import *
from gui.modules.ui_functions import UIFunctions
from gui.modules.app_functions import AppFunctions
from utils import logger
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None

class TheMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        rightButtons = self.ui
        modelPage = self.ui
        self.ui.ui_functions = UIFunctions(self.ui)

        # USE CUSTOM TITLE BAR
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "SnapStat"
        description = "Welcome to SnapStat!   A Simply To Use Finance Analysis Tool!"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_chat.clicked.connect(self.buttonClick)
        widgets.btn_admin.clicked.connect(self.buttonClick)
        widgets.btn_analysis.clicked.connect(self.buttonClick)
        widgets.btn_reboot.clicked.connect(self.buttonClick)
        widgets.btn_modeling.clicked.connect(self.buttonClick)
        widgets.btn_performance.clicked.connect(self.buttonClick)
        widgets.btn_cost.clicked.connect(self.buttonClick)
        widgets.btn_logs.clicked.connect(self.buttonClick)
        widgets.btn_export.clicked.connect(self.buttonClick)
        widgets.btn_models.clicked.connect(self.buttonClick)
        widgets.btn_share.clicked.connect(self.buttonClick)
        widgets.btn_adjustments.clicked.connect(self.buttonClick)
        modelPage.downloadButton.clicked.connect(self.buttonClick)
        widgets.chat_send_button.clicked.connect(self.buttonClick)        
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        self.useCustomTheme = True
        self.themeFile = "./gui/themes/dark.qss"

        # SET THEME AND HACKS
        if self.useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, self.themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post functions for clicked buttons
        rightButtons.themeSettingsBtn.clicked.connect(self.toggleTheme)        
    def toggleTheme(self):
        if not self.useCustomTheme:
            return

        if "dark" in self.themeFile:
            logger.info("Theme switched to Light Theme")
            self.themeFile = "./gui/themes/light.qss"
            new_icon_path = "./gui/images/icons/cil-sun.png"
            new_chat_path = "./gui/images/icons/cil-paper-plane-black.png"
        else:
            logger.info("Theme switched to Dark Theme")
            self.themeFile = "./gui/themes/dark.qss"
            new_icon_path = "./gui/images/icons/cil-moon.png"
            new_chat_path = "./gui/images/icons/cil-paper-plane.png"

        # Apply theme and hacks
        UIFunctions.theme(self, self.themeFile, True)
        AppFunctions.setThemeHack(self)
        new_icon = QIcon(new_icon_path)
        self.ui.themeSettingsBtn.setIcon(new_icon)
        
        # Apply theme and hacks to Chat Send Button Icon
        new_chat_icon = QIcon(new_chat_path)
        self.ui.chat_send_button.setIcon(new_chat_icon)
    
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        
        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home) # SET PAGE to HOME
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        if btnName == "btn_chat":
            widgets.stackedWidget.setCurrentWidget(widgets.chat) # SET PAGE to CHAT
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW ADMIN PAGE - DISABLED FOR NOW
        # if btnName == "btn_admin":
        #     widgets.stackedWidget.setCurrentWidget(widgets.widgets) # SET PAGE to WIDGETS
        #     UIFunctions.resetStyle(self, btnName)
        #     btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # SHOW Modeling PAGE
        if btnName == "btn_modeling":
            widgets.stackedWidget.setCurrentWidget(widgets.modeling) # Set Page to Modeling
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # SHOW PERFORMANCE PAGE
        if btnName == "btn_performance":
            widgets.stackedWidget.setCurrentWidget(widgets.performance) # Set Page to Performance
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # SHOW COST PAGE
        if btnName == "btn_cost":
            widgets.stackedWidget.setCurrentWidget(widgets.cost) # Set Page to Cost
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # SHOW LOGS PAGE
        if btnName == "btn_logs":
            logger.info("Logs Page needs to be built!")
            # widgets.stackedWidget.setCurrentWidget(widgets.logs) # Set Page to Logs
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        if btnName == "btn_export":
            logger.info("Export Function needs to be built!")

        if btnName == "btn_analysis":
            widgets.stackedWidget.setCurrentWidget(widgets.analysis) # Set Page to Analysis
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        if btnName == "btn_models":
            widgets.stackedWidget.setCurrentWidget(widgets.modelPage) # Set Page to Models
            UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # This is causing the selection to stay and not deselect after another button is pressed
        
        if btnName == "btn_share":
            logger.info("Share Page needs to be built!")
        
        if btnName == "downloadButton":
            logger.info("Download Models Function needs to be built!")
        
        if btnName == "btn_adjustments":
            widgets.stackedWidget.setCurrentWidget(widgets.adjustmentsPage) # Set Page to Adjustments
            UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # This is causing the selection to stay and not deselect after another button is pressed
        
        if btnName == "btn_reboot":
            logger.debug("Reboot Function needs to be built!")

        # LOG BTN NAME TO CONSOLE
        if btnName == "btn_admin":
            logger.debug(f'Button "{btnName}" clicked! - Disabled at the moment...')
        
        if btnName == 'chat_send_button':
            logger.debug(f'Button "{btnName}" pressed!')
            self.ui.ui_functions.send_message()
            


    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # LOG MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            logger.debug('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            logger.debug('Mouse click: RIGHT CLICK')