from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.md_check_box import MdCheckBox
from tests.QA.functionality.management.ui_alhambra.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_alhambra.utils.actions import find_elements
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class AdvancedPanel(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[@class='advanced-panel']")
        super(AdvancedPanel, self).__init__(locator, parent)

    @property
    def left_panel(self):
        return LeftPanel(self)

    @property
    def right_panel(self):
        return RightPanel(self)


class LeftPanel(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'left-panel')]")
        super(LeftPanel, self).__init__(locator, parent)

    @property
    def malware_tab(self):
        xpath = "//*[contains(@class, 'row') and descendant::*[contains(text(), 'Malware')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def operations_tab(self):
        xpath = "//*[contains(@class, 'row') and descendant::*[contains(text(), 'Operations')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def white_black_list_tab(self):
        xpath = "//*[contains(@class, 'row') and descendant::*[contains(text(), 'Whitelist / Blacklist')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def mitigation_tab(self):
        xpath = "//*[contains(@class, 'row') and descendant::*[contains(text(), 'Mitigation')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def administrative_tab(self):
        xpath = "//*[contains(@class, 'row') and descendant::*[contains(text(), 'Administrative')]]"
        return BaseElement(XPathLocator(xpath), self)

    def get_selected_tab_name(self):
        elem = TextElement(XPathLocator("//div[@* and ancestor::*[contains(@class, 'row active')]]"),self)
        return elem.get_text()


class AdvancedRow(BaseElement):
    def __init__(self, name, parent):
        locator = XPathLocator(
            "//*[contains(@class, 'row') and descendant::*[contains(@class, 'row-title') and contains(text(), '{}')]]".format(
                name))
        super(AdvancedRow, self).__init__(locator, parent)

    def _get_checkboxes_ids(self):
        checkbox = MdCheckBox('', self)
        elements = find_elements(checkbox)
        ids = list()
        for element in elements:
            current_id = element.get_attribute('id').partition('md-checkbox-')[2]
            ids.append(current_id)
        return ids

    @property
    def critical_checkbox(self):
        return MdCheckBox(self._get_checkboxes_ids()[0], self)

    @property
    def advisory_checkbox(self):
        return MdCheckBox(self._get_checkboxes_ids()[1], self)

    @property
    def information_checkbox(self):
        return MdCheckBox(self._get_checkboxes_ids()[2], self)


class RightPanel(BaseElement):

    malware_rows = ['Active', 'Mitigated', 'Blocked', 'Suspicious']
    operations_rows = ['Agent uninstall request', 'Agent uninstalled', 'Agent subscribed', 'Agent decommissioned',
                       'Recommission agent', 'Agent updated', 'User requested full log report',
                       'Agent uploaded full log report', 'Fetch files operations', 'Full disk scan operations']
    white_black_list_rows = ['New immune', 'Whitelist modified', 'Blacklist modified', 'Hash modified', 'Hash deleted']
    mitigation_rows = ['Kill', 'Quarantine', 'Remediate', 'Rollback', 'Shut down', 'Disconnect / reconnect network']
    administrative_rows = ['User added / modified / deleted', 'Management software updated',
                           'Threat policy mode modified', 'Suspicious policy mode modified',
                           'Configuration action modified', 'Immune modified', 'Agent software updated',
                           'Threat resolved', 'Suspicious activity resolved', 'Suspicious marked as threat',
                           'Auto decommission configuration modified', 'Auto decommission days modified',
                           'Disconnect from network modified', 'Notification option level modified',
                           'Event severity level modified', 'Notification recipients modified',
                           'Two Factor authentication modified', 'Monitor on write modified',
                           'Monitor on execute modified', 'Deep visibility setting modified',
                           'Cloud marked the suspicious activity as resolved', 'Cloud unresolved a threat',
                           'Scan New Agents Changed', 'Anti Tampering Modified', 'Snapshots Settings Modified',
                           'Agent UI Settings Modified', 'Agent Logging Aborted']

    categories = {'malware': malware_rows, 'operations': operations_rows, 'white_black_lists': white_black_list_rows,
                  'mitigation': mitigation_rows, 'administrative': administrative_rows}

    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'right-panel')]")
        super(RightPanel, self).__init__(locator, parent)

    def get_row_by_name(self, name):
        return AdvancedRow(name, self)
