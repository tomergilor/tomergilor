from slash import g
from slash_step import STEP

from Scripts import Config
from tests.QA.functionality.management.ui_bigben.pages.p_main.network_page.exclusions_page import ExclusionsTab
from tests.QA.functionality.management.ui_bigben.pages.p_main.network_page.exclusions_page.new_exclusion import \
    NewExclusionDialog, FileTypeExclusion, SignerIdentity, BrowserExclusion, PathExclusion, HashExclusion


def test_ui_exclusions_test(machine_generator):
    with STEP('Create additional site'):
        second_site_id = g.manager.create_site(name='second_site')['data']['id']

    with STEP('Create groups for first (default) site'):
        g.manager.create_group(name='group1')
        g.manager.create_group(name='group2')

    with STEP('Create groups for second site'):
        g.manager.create_group(site_id=second_site_id, name='group3')
        g.manager.create_group(site_id=second_site_id, name='group4')

    with STEP('Create policy for group'):
        g.manager.create_policy(group_id='')
        pass  # Waiting for backend implementing of this API call

    with STEP('Create policy for group'):
        g.manager.create_policy(site_id='')
        pass  # Waiting for backend implementing of this API call

    with STEP('install first agent'):
        agent_machine1 = machine_generator.get_new_agent_machine(g.installer_path,
                                                                 agent_settings=Config.get_agent_settings())

    with STEP('Add agent to group'):
        pass  # Waiting for backend implementing of this API call

#######################################################################################################################


#############################   Add all types of exclusions    #######################


    driver = g.driver

## Add new 'File type' exclusion
    with STEP('Click on file type button'):
        exclusion_tab = ExclusionsTab(driver)
        exclusion_tab.exclusion_types_bar.file_type.click()

    with STEP('Select OS (windows) Type'):
        dialog = NewExclusionDialog(driver)
        dialog.os_type_selector.select_by_text('Windows')

    with STEP('Select Exclusion type'):
        dialog.exclusion_type_selector.select_by_text('File Type')

    with STEP('Enter File type'):
        dialog = FileTypeExclusion(driver)
        dialog.filetype.enter_text('pdf')
        #FileTypeExclusion(driver).filetype.enter_text('pdf')

    with STEP('Enter Description'):
        dialog.description.enter_text('pdf_file')

    with STEP('Click save'):
        dialog.save_btn.click()

    with STEP('Delete the file type exclusion'):
        exclusion_tab.exclusion_list_area.grid.get_row_by_text('pdf_file').checkbox.check()
        exclusion_tab.exclusion_list_area.exclusion_toolbar.delete_selection_btn.click()


## Add new 'Signer identity' exclusion
    with STEP('Click on Signer Identity button'):
         exclusion_tab = ExclusionsTab(driver)
         exclusion_tab.exclusion_types_bar.signer_identity.click()

    with STEP('Select OS (windows) Type'):
         dialog.os_type_selector.select_by_text('Windows')

    with STEP('Enter Certificate ID'):  # enter WINRAR for example: WIN.RAR GMBH
        dialog = SignerIdentity(driver)
        dialog.CertificateID.enter_text('WIN.RAR GMBH')

    with STEP('Enter Description'):
        dialog.description.enter_text('Entered WIN.RAR GMBH signer Identiry')

    with STEP('Click save'):
        dialog.save_btn.click()

    with STEP('Delete the Signer identity exclusion'):
        exclusion_tab.exclusion_list_area.grid.get_row_by_text('WIN.RAR GMBH').checkbox.check()
        exclusion_tab.exclusion_list_area.exclusion_toolbar.delete_selection_btn.click()


## Add new 'Browser Type' exclusion
    with STEP('Click on Browser Type button'):
        exclusion_tab.exclusion_types_bar.browser.click()

    with STEP('Select OS (windows) Type'):
        dialog.os_type_selector.select_by_text('Windows')

    with STEP('Select Browser'):        #chrome
        dialog = BrowserExclusion(driver)
        dialog.browser_type_selector.select_by_text('Chrome')

    with STEP('Enter Description'):
        dialog.description.enter_text('Chrome browser has been chosen')

    with STEP('Click save'):
        dialog.save_btn.click()

    with STEP('Delete the Browser Type exclusion'):
        exclusion_tab.exclusion_list_area.grid.get_row_by_text('Chrome').checkbox.check()
        exclusion_tab.exclusion_list_area.exclusion_toolbar.delete_selection_btn.click()


## Add new 'Path' exclusion
    with STEP('Click on Path button'):
         exclusion_tab.exclusion_types_bar.path.click()

    with STEP('Select OS (windows) Type'):
         dialog.os_type_selector.select_by_text('Windows')

    with STEP('Enter path'):        # C:\Temp
        dialog.description.enter_text('C:\Temp')

    with STEP('monitor'):
        dialog = PathExclusion(driver)
        dialog.include_monitor_checkbox.click()

    with STEP('include subfolders'):
        dialog.include_subfolders_checkbox.click()

    with STEP('Enter Description'):
        dialog.description.enter_text('Added path: C:\Temp')

    with STEP('Click save'):
        dialog.save_btn.click()

    with STEP('Delete the Path exclusion'):
        exclusion_tab.exclusion_list_area.grid.get_row_by_text('C:\Temp').checkbox.check()
        exclusion_tab.exclusion_list_area.exclusion_toolbar.delete_selection_btn.click()


## Add new 'Hash' exclusion
    with STEP('Click on Hash button'):
         exclusion_tab.exclusion_types_bar.hash.click()

    with STEP('Select OS (windows) Type'):
         dialog.os_type_selector.select_by_text('Windows')

    with STEP('Enter White Hash number'):           # 9999999999999999999999999999999999999999
        dialog = HashExclusion(driver)
        dialog.hash_exclusion.enter_text('9999999999999999999999999999999999999999')

    with STEP('Enter Description'):
        dialog.description.enter_text('Added hash: 9999999999999999999999999999999999999999 ')

    with STEP('Click Save'):
        dialog.save_btn.click()

    with STEP('Delete the White Hash'):
        exclusion_tab.exclusion_list_area.grid.get_row_by_text('9999999999999999999999999999999999999999').checkbox.check()
        exclusion_tab.exclusion_list_area.exclusion_toolbar.delete_selection_btn.click()



############################################################################

#######################  Matrix tests   ####################################


    ## 1.   Add Global Tenant + 2 sites + 4 Groups (2 for each site) - Gosha - Verify that No exclusion sent to agents


    ## 2.   Add Path exclusion to Tenant only  - Goash - Verify exclusion sent to entire agents






















    # with STEP('Click network tab'):
    #     MainPage(driver).left_side_tabs.network_tab.click()
    #     NetworkPage(driver).tabs_panel.exclusions_tab.click()
    #     exclusion_tab = ExclusionsTab(driver)
    #
    #     exclusion_tab.exclusion_types_bar.path.click()
    #     exclusion_tab.exclusion_list_area.exclusion_toolbar.new_exclusion_btn.click()
    #     dialog = NewExclusionDialog(driver)
    #     dialog.path.enter_text('C:/temp')
    #     dialog.os_type_selector.select_by_text('windows')
    #
    #     dialog.save_btn.click()
    #     assert exclusion_tab.exclusion_list_area.grid.get_row_by_text('new_exclusion').is_in_dom()

