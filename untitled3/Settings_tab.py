from tests.QA.functionality.management.ui_alhambra.page_types.tab import TopTab
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement


class SettingsTabsPanel(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//nav[@class='menu-container']")
        super(SettingsTabsPanel, self).__init__(locator, parent)

    @property
    def policies_tab(self):
        return TopTab('Policies', self)

    @property
    def configuration_tab(self):
        return TopTab('Configuration', self)

    @property
    def exclusions_tab(self):
        return TopTab('Exclusions', self)

    @property
    def updates_tab(self):
        return TopTab('Updates', self)

    @property
    def notifications_tab(self):
        return TopTab('Notifications', self)

    @property
    def users_tab(self):
        return TopTab('Users', self)

    @property
    def integrations_tab(self):
        return TopTab('Integrations', self)
