import random
import string


# tenant = ''.join([random.choice(string.lowercase) for i in xrange(4)])      # creates rundom 6 sybmols string
# tenant = 'tenant_{}'.format(tenant)
# print tenant




# import random
# #for x in range(10):
# rand = random.randint(1,101)
# print rand
#
# suffix = ''.join([random.choice(string.lowercase) for i in xrange(4)])      # creates rundom 6 sybmols string
# tenant = 'Tenant_{}'.format(suffix )
# print tenant
#
# suffix = ''.join([random.choice(string.lowercase) for i in xrange(4)])      # creates rundom 6 sybmols string
# site1 = 'Site1_{}'.format(suffix )
# print site1
#
# suffix = ''.join([random.choice(string.lowercase) for i in xrange(4)])      # creates rundom 6 sybmols string
# site2 = 'Site2_{}'.format(suffix )
# print site2
#
# suffix = ''.join([random.choice(string.lowercase) for i in xrange(4)])      # creates rundom 6 sybmols string
# Group1 = 'Group1_{}'.format(suffix )
# print Group1
#
# suffix = ''.join([random.choice(string.lowercase) for i in xrange(4)])      # creates rundom 6 sybmols string
# Group2 = 'Group2_{}'.format(suffix )
# print Group2
#


#   AutomationID = "SitesDropdown"
#   AutomationID = "SearchField"

# def get_random_string(range=6):
#     return ''.join([random.choice(string.lowercase) for i in xrange(range)])
#
# with STEP('Update global policy when group has one'):
#     site_name = get_random_string()


def get_random_string(range=6):
    return ''.join([random.choice(string.lowercase) for i in xrange(range)])

with STEP('create new group1 name'):
rnd = get_random_string()
group1 = 'group1_{}'.format(rnd)
print group1

