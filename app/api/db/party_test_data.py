from app.api.model.party import Party


# dummy data for the tests
party = Party(party_name='example name',
              hq_address='example location')
party_holder = party.party_jsonified()

null_party_name = Party(
    party_name='', hq_address='example location')
null_party_name_holder = null_party_name.party_jsonified()

null_party_hq = Party(party_name='example name', hq_address='')
null_party_hq_holder = null_party_hq.party_jsonified()

null_party_entries = Party(party_name='', hq_address='')
null_party_entries_holder = null_party_entries.party_jsonified()

int_party_name = Party(
    party_name='12233', hq_address='example location')
int_party_name_holder = int_party_name.party_jsonified()
