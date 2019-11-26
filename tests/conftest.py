import pytest

from redswitch.esl import ESLAsp
from redswitch.esl import ESLBot


@pytest.fixture
def asp_esl(mocker):
    mocker.patch('redswitch.esl.rediscluster.StrictRedisCluster',
                 mocker.MagicMock())

    mocker.patch('redswitch.esl.switchy.Client', mocker.MagicMock())
    mocker.patch('redswitch.esl.switchy.EventListener', mocker.MagicMock())

    return ESLAsp('redis://host:6379', mocker.MagicMock(), 'ESL_URL',
                  'ESL_PORT', 'ESL_PASSWORD')


@pytest.fixture
def bot_esl(mocker):
    mocker.patch('redswitch.esl.rediscluster.StrictRedisCluster',
                 mocker.MagicMock())

    mocker.patch('redswitch.esl.switchy.Client', mocker.MagicMock())
    mocker.patch('redswitch.esl.switchy.EventListener', mocker.MagicMock())

    return ESLBot('redis://host:6379', mocker.MagicMock(), 'ESL_URL',
                  'ESL_PORT', 'ESL_PASSWORD')


class MockESLEvent:
    def __init__(self, data):
        self.event = data

    def getHeader(self, key):
        return self.event[key]


@pytest.fixture
def answer_event():
    # pylint: disable=line-too-long
    return MockESLEvent({
        'Event-Name': 'CHANNEL_ANSWER',
        'Core-UUID': '233e80d6-aec3-11e7-ada4-8d3cbd6c098c',
        'FreeSWITCH-Hostname': 'vadertest',
        'FreeSWITCH-Switchname': 'vadertest',
        'FreeSWITCH-IPv4': '174.36.124.247',
        'FreeSWITCH-IPv6': '%3A%3A1',
        'Event-Date-Local': '2017-11-20%2022%3A45%3A09',
        'Event-Date-GMT': 'Mon,%2020%20Nov%202017%2022%3A45%3A09%20GMT',
        'Event-Date-Timestamp': '1511217909772147',
        'Event-Calling-File': 'switch_channel.c',
        'Event-Calling-Function': 'switch_channel_perform_mark_answered',
        'Event-Calling-Line-Number': '3706',
        'Event-Sequence': '5026896',
        'Channel-State': 'CS_EXECUTE',
        'Channel-Call-State': 'EARLY',
        'Channel-State-Number': '4',
        'Channel-Name': 'sofia/external/14157697098',
        'Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Call-Direction': 'outbound',
        'Presence-Call-Direction': 'outbound',
        'Channel-HIT-Dialplan': 'true',
        'Channel-Call-UUID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Answer-State': 'answered',
        'Channel-Read-Codec-Name': 'PCMU',
        'Channel-Read-Codec-Rate': '8000',
        'Channel-Read-Codec-Bit-Rate': '64000',
        'Channel-Write-Codec-Name': 'PCMU',
        'Channel-Write-Codec-Rate': '8000',
        'Channel-Write-Codec-Bit-Rate': '64000',
        'Caller-Direction': 'outbound',
        'Caller-Logical-Direction': 'outbound',
        'Caller-Caller-ID-Name': 'Outbound%20Call',
        'Caller-Caller-ID-Number': '14157697098',
        'Caller-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Caller-Orig-Caller-ID-Number': '16057819836',
        'Caller-Callee-ID-Name': 'Outbound%20Call',
        'Caller-Callee-ID-Number': '16057819836',
        'Caller-Network-Addr': '174.36.124.229',
        'Caller-ANI': '16057819836',
        'Caller-Destination-Number': '14157697098',
        'Caller-Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Caller-Source': 'src/switch_ivr_originate.c',
        'Caller-Context': 'default',
        'Caller-Channel-Name': 'sofia/external/14157697098',
        'Caller-Profile-Index': '1',
        'Caller-Profile-Created-Time': '1511217894092090',
        'Caller-Channel-Created-Time': '1511217894092090',
        'Caller-Channel-Answered-Time': '1511217909772147',
        'Caller-Channel-Progress-Time': '0',
        'Caller-Channel-Progress-Media-Time': '1511217899272093',
        'Caller-Channel-Hangup-Time': '0',
        'Caller-Channel-Transfer-Time': '0',
        'Caller-Channel-Resurrect-Time': '0',
        'Caller-Channel-Bridged-Time': '1511217899272093',
        'Caller-Channel-Last-Hold': '0',
        'Caller-Channel-Hold-Accum': '0',
        'Caller-Screen-Bit': 'true',
        'Caller-Privacy-Hide-Name': 'false',
        'Caller-Privacy-Hide-Number': 'false',
        'Other-Type': 'originatee',
        'Other-Leg-Direction': 'outbound',
        'Other-Leg-Logical-Direction': 'inbound',
        'Other-Leg-Caller-ID-Name': 'Outbound%20Call',
        'Other-Leg-Caller-ID-Number': '14157697098',
        'Other-Leg-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Other-Leg-Orig-Caller-ID-Number': '16057819836',
        'Other-Leg-Callee-ID-Name': 'Outbound%20Call',
        'Other-Leg-Callee-ID-Number': '16057819836',
        'Other-Leg-Network-Addr': '174.36.124.229',
        'Other-Leg-ANI': '16057819836',
        'Other-Leg-Destination-Number': '16057819836',
        'Other-Leg-Unique-ID': '6f21a816-ce44-11e7-bbf7-8d3cbd6c098c',
        'Other-Leg-Source': 'src/switch_ivr_originate.c',
        'Other-Leg-Context': 'default',
        'Other-Leg-Channel-Name': 'sofia/external/16057819836',
        'Other-Leg-Profile-Created-Time': '1511217897552138',
        'Other-Leg-Channel-Created-Time': '1511217897552138',
        'Other-Leg-Channel-Answered-Time': '1511217899272093',
        'variable_direction': 'outbound',
        'variable_is_outbound': 'true',
        'variable_uuid': '09d65f26-cece-11e7-b742-8d3cbd6c098c',
        'variable_session_id': '89769',
        'variable_sip_gateway_name': 'opensips',
        'variable_sip_invite_domain': 'echelonfs.sip.talkiq.net',
        'variable_sip_profile_name': 'gateway',
        'variable_video_media_flow': 'sendrecv',
        'variable_channel_name': 'sofia/external/16057819836',
        'variable_sip_destination_url': 'sip%3A16057819836%40sip.talkiq.net',
        'variable_sip_h_Accuvit-User-ID': '005j000000C8FKUAA3',
        'variable_sip_h_X-TalkIQ-Callprovider': 'shifty',
        'variable_sip_h_Accuvit-Dial-ID': '1337',
        'variable_sip_h_X-switchy_originating_session': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_sip_h_Accuvit-Organization-ID': '00Dj0000001noV5EAI',
        'variable_sip_h_X-switchy_app': 'de75affe-cecc-11e7-8174-0242acff0008',
        'variable_max_forwards': '70',
        'variable_originator_codec': 'PCMU%408000h%4020i',
        'variable_originator': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_switch_m_sdp': 'v%3D0%0D%0Ao%3DSonus_UAC%20904353%2051611%20IN%20IP4%2067.231.13.146%0D%0As%3DSIP%20Media%20Capabilities%0D%0Ac%3DIN%20IP4%2067.231.13.88%0D%0At%3D0%200%0D%0Am%3Daudio%2010998%20RTP/AVP%200%20101%0D%0Aa%3Drtpmap%3A0%20PCMU/8000%0D%0Aa%3Drtpmap%3A101%20telephone-event/8000%0D%0Aa%3Dfmtp%3A101%200-15%0D%0Aa%3Dptime%3A20%0D%0A',
        'variable_call-side': '1',
        'variable_dial_id': '1337',
        'variable_sip_h_Accuvit-Dial-Side': '1',
        'variable_ignore_early_media': 'False',
        'variable_originate_early_media': 'true',
        'variable_originating_leg_uuid': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_rtp_local_sdp_str': 'v%3D0%0D%0Ao%3DFreeSWITCH%201511259868%201511259869%20IN%20IP4%20174.36.124.247%0D%0As%3DFreeSWITCH%0D%0Ac%3DIN%20IP4%20174.36.124.247%0D%0At%3D0%200%0D%0Am%3Daudio%2017130%20RTP/AVP%200%20101%2013%0D%0Aa%3Drtpmap%3A0%20PCMU/8000%0D%0Aa%3Drtpmap%3A101%20telephone-event/8000%0D%0Aa%3Dfmtp%3A101%200-16%0D%0Aa%3Drtpmap%3A13%20CN/8000%0D%0Aa%3Dptime%3A20%0D%0Aa%3Dsendrecv%0D%0A',
        'variable_sip_outgoing_contact_uri': '%3Csip%3Agw%2Bopensips%40174.36.124.247%3A5080%3Btransport%3Dudp%3Bgw%3Dopensips%3E',
        'variable_sip_req_uri': '16057819836%40sip.talkiq.net',
        'variable_sofia_profile_name': 'external',
        'variable_recovery_profile_name': 'external',
        'variable_audio_media_flow': 'sendrecv',
        'variable_rtp_use_codec_string': 'PCMU%408000h%4020i',
        'variable_rtp_audio_recv_pt': '0',
        'variable_rtp_use_codec_name': 'PCMU',
        'variable_rtp_use_codec_rate': '8000',
        'variable_rtp_use_codec_ptime': '20',
        'variable_rtp_use_codec_channels': '1',
        'variable_rtp_last_audio_codec_string': 'PCMU%408000h%4020i%401c',
        'variable_read_codec': 'PCMU',
        'variable_original_read_codec': 'PCMU',
        'variable_read_rate': '8000',
        'variable_original_read_rate': '8000',
        'variable_call_uuid': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
    })


@pytest.fixture
def bridge_event():
    # pylint: disable=line-too-long
    return MockESLEvent({
        'Event-Name': 'CHANNEL_BRIDGE',
        'Core-UUID': '233e80d6-aec3-11e7-ada4-8d3cbd6c098c',
        'FreeSWITCH-Hostname': 'vadertest',
        'FreeSWITCH-Switchname': 'vadertest',
        'FreeSWITCH-IPv4': '174.36.124.247',
        'FreeSWITCH-IPv6': '%3A%3A1',
        'Event-Date-Local': '2017-11-20%2022%3A44%3A59',
        'Event-Date-GMT': 'Mon,%2020%20Nov%202017%2022%3A44%3A59%20GMT',
        'Event-Date-Timestamp': '1511217899272093',
        'Event-Calling-File': 'switch_ivr_bridge.c',
        'Event-Calling-Function': 'switch_ivr_multi_threaded_bridge',
        'Event-Calling-Line-Number': '1501',
        'Event-Sequence': '5026891',
        'Bridge-A-Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Bridge-B-Unique-ID': '6f21a816-ce44-11e7-bbf7-8d3cbd6c098c',
        'Channel-State': 'CS_EXECUTE',
        'Channel-Call-State': 'EARLY',
        'Channel-State-Number': '4',
        'Channel-Name': 'sofia/external/14157697098',
        'Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Call-Direction': 'outbound',
        'Presence-Call-Direction': 'outbound',
        'Channel-HIT-Dialplan': 'true',
        'Channel-Call-UUID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Answer-State': 'early',
        'Channel-Read-Codec-Name': 'PCMU',
        'Channel-Read-Codec-Rate': '8000',
        'Channel-Read-Codec-Bit-Rate': '64000',
        'Channel-Write-Codec-Name': 'PCMU',
        'Channel-Write-Codec-Rate': '8000',
        'Channel-Write-Codec-Bit-Rate': '64000',
        'Caller-Direction': 'outbound',
        'Caller-Logical-Direction': 'outbound',
        'Caller-Caller-ID-Name': 'Outbound%20Call',
        'Caller-Caller-ID-Number': '14157697098',
        'Caller-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Caller-Orig-Caller-ID-Number': '16057819836',
        'Caller-Callee-ID-Name': 'Outbound%20Call',
        'Caller-Callee-ID-Number': '16057819836',
        'Caller-Network-Addr': '174.36.124.229',
        'Caller-ANI': '16057819836',
        'Caller-Destination-Number': '14157697098',
        'Caller-Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Caller-Source': 'src/switch_ivr_originate.c',
        'Caller-Context': 'default',
        'Caller-Channel-Name': 'sofia/external/14157697098',
        'Caller-Profile-Index': '1',
        'Caller-Profile-Created-Time': '1511217894092090',
        'Caller-Channel-Created-Time': '1511217894092090',
        'Caller-Channel-Answered-Time': '0',
        'Caller-Channel-Progress-Time': '0',
        'Caller-Channel-Progress-Media-Time': '1511217899272093',
        'Caller-Channel-Hangup-Time': '0',
        'Caller-Channel-Transfer-Time': '0',
        'Caller-Channel-Resurrect-Time': '0',
        'Caller-Channel-Bridged-Time': '1511217899272093',
        'Caller-Channel-Last-Hold': '0',
        'Caller-Channel-Hold-Accum': '0',
        'Caller-Screen-Bit': 'true',
        'Caller-Privacy-Hide-Name': 'false',
        'Caller-Privacy-Hide-Number': 'false',
        'Other-Type': 'originatee',
        'Other-Leg-Direction': 'outbound',
        'Other-Leg-Logical-Direction': 'inbound',
        'Other-Leg-Caller-ID-Name': 'Outbound%20Call',
        'Other-Leg-Caller-ID-Number': '14157697098',
        'Other-Leg-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Other-Leg-Orig-Caller-ID-Number': '16057819836',
        'Other-Leg-Callee-ID-Name': 'Outbound%20Call',
        'Other-Leg-Callee-ID-Number': '16057819836',
        'Other-Leg-Network-Addr': '174.36.124.229',
        'Other-Leg-ANI': '16057819836',
        'Other-Leg-Destination-Number': '16057819836',
        'Other-Leg-Unique-ID': '6f21a816-ce44-11e7-bbf7-8d3cbd6c098c',
        'Other-Leg-Source': 'src/switch_ivr_originate.c',
        'Other-Leg-Context': 'default',
        'Other-Leg-Channel-Name': 'sofia/external/16057819836',
        'Other-Leg-Profile-Created-Time': '1511217897552138',
        'variable_channel_name': 'sofia/external/16057819836',
        'variable_sip_destination_url': 'sip%3A16057819836%40sip.talkiq.net',
        'variable_sip_h_Accuvit-User-ID': '005j000000C8FKUAA3',
        'variable_sip_h_X-TalkIQ-Callprovider': 'shifty',
        'variable_sip_h_Accuvit-Dial-ID': '1337',
        'variable_sip_h_X-switchy_originating_session': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_sip_h_Accuvit-Organization-ID': '00Dj0000001noV5EAI',
        'variable_sip_h_X-switchy_app': 'de75affe-cecc-11e7-8174-0242acff0008',
        'variable_max_forwards': '70',
        'variable_originator_codec': 'PCMU%408000h%4020i',
        'variable_originator': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_switch_m_sdp': 'v%3D0%0D%0Ao%3DSonus_UAC%20904353%2051611%20IN%20IP4%2067.231.13.146%0D%0As%3DSIP%20Media%20Capabilities%0D%0Ac%3DIN%20IP4%2067.231.13.88%0D%0At%3D0%200%0D%0Am%3Daudio%2010998%20RTP/AVP%200%20101%0D%0Aa%3Drtpmap%3A0%20PCMU/8000%0D%0Aa%3Drtpmap%3A101%20telephone-event/8000%0D%0Aa%3Dfmtp%3A101%200-15%0D%0Aa%3Dptime%3A20%0D%0A',
        'variable_call-side': '1',
        'variable_dial_id': '1337',
        'variable_sip_h_Accuvit-Dial-Side': '1',
        'variable_ignore_early_media': 'False',
        'variable_originate_early_media': 'true',
        'variable_originating_leg_uuid': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_rtp_local_sdp_str': 'v%3D0%0D%0Ao%3DFreeSWITCH%201511259868%201511259869%20IN%20IP4%20174.36.124.247%0D%0As%3DFreeSWITCH%0D%0Ac%3DIN%20IP4%20174.36.124.247%0D%0At%3D0%200%0D%0Am%3Daudio%2017130%20RTP/AVP%200%20101%2013%0D%0Aa%3Drtpmap%3A0%20PCMU/8000%0D%0Aa%3Drtpmap%3A101%20telephone-event/8000%0D%0Aa%3Dfmtp%3A101%200-16%0D%0Aa%3Drtpmap%3A13%20CN/8000%0D%0Aa%3Dptime%3A20%0D%0Aa%3Dsendrecv%0D%0A',
        'variable_sip_outgoing_contact_uri': '%3Csip%3Agw%2Bopensips%40174.36.124.247%3A5080%3Btransport%3Dudp%3Bgw%3Dopensips%3E',
        'variable_sip_req_uri': '16057819836%40sip.talkiq.net',
        'variable_sofia_profile_name': 'external',
        'variable_recovery_profile_name': 'external',
        'variable_audio_media_flow': 'sendrecv',
        'variable_rtp_use_codec_string': 'PCMU%408000h%4020i',
        'variable_rtp_audio_recv_pt': '0',
        'variable_rtp_use_codec_name': 'PCMU',
        'variable_rtp_use_codec_rate': '8000',
        'variable_rtp_use_codec_ptime': '20',
        'variable_rtp_use_codec_channels': '1',
        'variable_rtp_last_audio_codec_string': 'PCMU%408000h%4020i%401c',
        'variable_read_codec': 'PCMU',
        'variable_original_read_codec': 'PCMU',
        'variable_read_rate': '8000',
        'variable_original_read_rate': '8000',
        'variable_call_uuid': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
    })


@pytest.fixture
def channel_create_event():
    # pylint: disable=line-too-long
    return MockESLEvent({
        'Event-Name': 'CHANNEL_CREATE',
        'Core-UUID': '233e80d6-aec3-11e7-ada4-8d3cbd6c098c',
        'FreeSWITCH-Hostname': 'vadertest',
        'FreeSWITCH-Switchname': 'vadertest',
        'FreeSWITCH-IPv4': '174.36.124.247',
        'FreeSWITCH-IPv6': '%3A%3A1',
        'Event-Date-Local': '2017-11-20%2022%3A44%3A54',
        'Event-Date-GMT': 'Mon,%2020%20Nov%202017%2022%3A44%3A54%20GMT',
        'Event-Date-Timestamp': '1511217894092090',
        'Event-Calling-File': 'switch_core_state_machine.c',
        'Event-Calling-Function': 'switch_core_session_run',
        'Event-Calling-Line-Number': '588',
        'Event-Sequence': '5026852',
        'Channel-State': 'CS_INIT',
        'Channel-Call-State': 'DOWN',
        'Channel-State-Number': '2',
        'Channel-Name': 'sofia/external/14157697098',
        'Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Call-Direction': 'outbound',
        'Presence-Call-Direction': 'outbound',
        'Channel-HIT-Dialplan': 'false',
        'Channel-Call-UUID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Answer-State': 'ringing',
        'Caller-Direction': 'outbound',
        'Caller-Logical-Direction': 'outbound',
        'Caller-Caller-ID-Name': 'Mr_Switchy',
        'Caller-Caller-ID-Number': '16057819836',
        'Caller-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Caller-Orig-Caller-ID-Number': '16057819836',
        'Caller-Callee-ID-Name': 'Outbound%20Call',
        'Caller-Callee-ID-Number': '14157697098',
        'Caller-ANI': '16057819836',
        'Caller-Destination-Number':  '14157697098',
        'Caller-Unique-ID': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'Caller-Source': 'src/switch_ivr_originate.c',
        'Caller-Context': 'default',
        'Caller-Channel-Name': 'sofia/external/14157697098',
        'Caller-Profile-Index': '1',
        'Caller-Profile-Created-Time': '1511217894092090',
        'Caller-Channel-Created-Time': '1511217894092090',
        'Caller-Channel-Answered-Time': '0',
        'Caller-Channel-Progress-Time': '0',
        'Caller-Channel-Progress-Media-Time': '0',
        'Caller-Channel-Hangup-Time': '0',
        'Caller-Channel-Transfer-Time': '0',
        'Caller-Channel-Resurrect-Time': '0',
        'Caller-Channel-Bridged-Time': '0',
        'Caller-Channel-Last-Hold': '0',
        'Caller-Channel-Hold-Accum': '0',
        'Caller-Screen-Bit': 'true',
        'Caller-Privacy-Hide-Name': 'false',
        'Caller-Privacy-Hide-Number': 'false',
        'variable_direction': 'outbound',
        'variable_is_outbound': 'true',
        'variable_uuid': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'variable_call_uuid': 'e77068a4-60b2-4e70-a903-2576cfa5ca07',
        'variable_session_id': '88061',
        'variable_sip_gateway_name': 'opensips',
        'variable_sip_invite_domain': 'echelonfs.sip.talkiq.net',
        'variable_sip_local_network_addr': '174.36.124.247',
        'variable_sip_profile_name': 'gateway',
        'variable_video_media_flow': 'sendrecv',
        'variable_audio_media_flow': 'sendrecv',
        'variable_channel_name': 'sofia/external/14157697098',
        'variable_sip_destination_url': 'sip%3A14157697098%40sip.talkiq.net',
        'variable_originate_timeout': '60',
        'variable_ignore_display_updates': 'true',
        'variable_sip_h_Accuvit-Dial-Side': '0',
        'variable_origination_caller_id_number': '16057819836',
        'variable_call-side': '0',
        'variable_dial_id': '1337',
        'variable_origination_caller_id_name': 'Mr_Switchy',
        'variable_sip_h_Accuvit-Dial-ID': '1337',
        'variable_sip_h_X-switchy_app': 'ca758216-ce3d-11e7-b1dd-0242acff0008',
        'variable_sip_h_X-TalkIQ-Callprovider': 'shifty',
        'variable_origination_callee_id_number': '14157697098',
        'variable_origination_uuid': 'e77068a4-60b2-4e70-a903-2576cfa5ca07'
    })


@pytest.fixture
def hangup_event():
    # pylint: disable=line-too-long
    return MockESLEvent({
        'Event-Name': 'CHANNEL_HANGUP',
        'Core-UUID': '233e80d6-aec3-11e7-ada4-8d3cbd6c098c',
        'FreeSWITCH-Hostname': 'vadertest',
        'FreeSWITCH-Switchname': 'vadertest',
        'FreeSWITCH-IPv4': '174.36.124.247',
        'FreeSWITCH-IPv6': '%3A%3A1',
        'Event-Date-Local': '2017-11-21%2015%3A10%3A20',
        'Event-Date-GMT': 'Tue,%2021%20Nov%202017%2015%3A10%3A20%20GMT',
        'Event-Date-Timestamp': '1511277020872091',
        'Event-Calling-File': 'switch_channel.c',
        'Event-Calling-Function': 'switch_channel_perform_hangup',
        'Event-Calling-Line-Number': '3283',
        'Event-Sequence': '5108249',
        'Channel-State': 'CS_EXECUTE',
        'Channel-Call-State': 'ACTIVE',
        'Channel-State-Number': '10',
        'Channel-Name': 'sofia/external/14157697098',
        'Unique-ID': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'Call-Direction': 'outbound',
        'Presence-Call-Direction': 'outbound',
        'Channel-HIT-Dialplan': 'true',
        'Channel-Call-UUID': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'Answer-State': 'hangup',
        'Hangup-Cause': 'NORMAL_CLEARING',
        'Channel-Read-Codec-Name': 'PCMU',
        'Channel-Read-Codec-Rate': '8000',
        'Channel-Read-Codec-Bit-Rate': '64000',
        'Channel-Write-Codec-Name': 'PCMU',
        'Channel-Write-Codec-Rate': '8000',
        'Channel-Write-Codec-Bit-Rate': '64000',
        'Caller-Direction': 'outbound',
        'Caller-Logical-Direction': 'outbound',
        'Caller-Caller-ID-Name': 'Outbound%20Call',
        'Caller-Caller-ID-Number': '14157697098',
        'Caller-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Caller-Orig-Caller-ID-Number': '16057819836',
        'Caller-Callee-ID-Name': 'Outbound%20Call',
        'Caller-Callee-ID-Number': '16057819836',
        'Caller-Network-Addr': '174.36.124.229',
        'Caller-ANI': '16057819836',
        'Caller-Destination-Number': '14157697098',
        'Caller-Unique-ID': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'Caller-Source': 'src/switch_ivr_originate.c',
        'Caller-Context': 'default',
        'Caller-Channel-Name': 'sofia/external/14157697098',
        'Caller-Profile-Index': '1',
        'Caller-Profile-Created-Time': '1511276995392112',
        'Caller-Channel-Created-Time': '1511276995392112',
        'Caller-Channel-Answered-Time': '1511277007572171',
        'Caller-Channel-Progress-Time': '0',
        'Caller-Channel-Progress-Media-Time': '1511276999992081',
        'Caller-Channel-Hangup-Time': '0',
        'Caller-Channel-Transfer-Time': '0',
        'Caller-Channel-Resurrect-Time': '0',
        'Caller-Channel-Bridged-Time': '1511276999992081',
        'Caller-Channel-Last-Hold': '0',
        'Caller-Channel-Hold-Accum': '0',
        'Caller-Screen-Bit': 'true',
        'Caller-Privacy-Hide-Name': 'false',
        'Caller-Privacy-Hide-Number': 'false',
        'Other-Type': 'originatee',
        'Other-Leg-Direction': 'outbound',
        'Other-Leg-Logical-Direction': 'inbound',
        'Other-Leg-Caller-ID-Name': 'Outbound%20Call',
        'Other-Leg-Caller-ID-Number': '14157697098',
        'Other-Leg-Orig-Caller-ID-Name': 'Mr_Switchy',
        'Other-Leg-Orig-Caller-ID-Number': '16057819836',
        'Other-Leg-Callee-ID-Name': 'Outbound%20Call',
        'Other-Leg-Callee-ID-Number': '16057819836',
        'Other-Leg-Network-Addr': '174.36.124.229',
        'Other-Leg-ANI': '16057819836',
        'Other-Leg-Destination-Number': '16057819836',
        'Other-Leg-Unique-ID': '09d65f26-cece-11e7-b742-8d3cbd6c098c',
        'Other-Leg-Source': 'src/switch_ivr_originate.c',
        'Other-Leg-Context': 'default',
        'Other-Leg-Channel-Name': 'sofia/external/16057819836',
        'Other-Leg-Profile-Created-Time': '1511276998152089',
        'Other-Leg-Channel-Created-Time': '1511276998152089',
        'variable_direction': 'outbound',
        'variable_is_outbound': 'true',
        'variable_uuid': '09d65f26-cece-11e7-b742-8d3cbd6c098c',
        'variable_session_id': '89769',
        'variable_sip_gateway_name': 'opensips',
        'variable_sip_invite_domain': 'echelonfs.sip.talkiq.net',
        'variable_sip_profile_name': 'gateway',
        'variable_video_media_flow': 'sendrecv',
        'variable_channel_name': 'sofia/external/16057819836',
        'variable_sip_destination_url': 'sip%3A16057819836%40sip.talkiq.net',
        'variable_sip_h_Accuvit-User-ID': '005j000000C8FKUAA3',
        'variable_sip_h_X-TalkIQ-Callprovider': 'shifty',
        'variable_sip_h_Accuvit-Dial-ID': '1337',
        'variable_sip_h_X-switchy_originating_session': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_sip_h_Accuvit-Organization-ID': '00Dj0000001noV5EAI',
        'variable_sip_h_X-switchy_app': 'de75affe-cecc-11e7-8174-0242acff0008',
        'variable_max_forwards': '70',
        'variable_originator_codec': 'PCMU%408000h%4020i',
        'variable_originator': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_switch_m_sdp': 'v%3D0%0D%0Ao%3DSonus_UAC%20904353%2051611%20IN%20IP4%2067.231.13.146%0D%0As%3DSIP%20Media%20Capabilities%0D%0Ac%3DIN%20IP4%2067.231.13.88%0D%0At%3D0%200%0D%0Am%3Daudio%2010998%20RTP/AVP%200%20101%0D%0Aa%3Drtpmap%3A0%20PCMU/8000%0D%0Aa%3Drtpmap%3A101%20telephone-event/8000%0D%0Aa%3Dfmtp%3A101%200-15%0D%0Aa%3Dptime%3A20%0D%0A',
        'variable_call-side': '1',
        'variable_dial_id': '1337',
        'variable_sip_h_Accuvit-Dial-Side': '1',
        'variable_ignore_early_media': 'False',
        'variable_originate_early_media': 'true',
        'variable_originating_leg_uuid': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
        'variable_rtp_local_sdp_str': 'v%3D0%0D%0Ao%3DFreeSWITCH%201511259868%201511259869%20IN%20IP4%20174.36.124.247%0D%0As%3DFreeSWITCH%0D%0Ac%3DIN%20IP4%20174.36.124.247%0D%0At%3D0%200%0D%0Am%3Daudio%2017130%20RTP/AVP%200%20101%2013%0D%0Aa%3Drtpmap%3A0%20PCMU/8000%0D%0Aa%3Drtpmap%3A101%20telephone-event/8000%0D%0Aa%3Dfmtp%3A101%200-16%0D%0Aa%3Drtpmap%3A13%20CN/8000%0D%0Aa%3Dptime%3A20%0D%0Aa%3Dsendrecv%0D%0A',
        'variable_sip_outgoing_contact_uri': '%3Csip%3Agw%2Bopensips%40174.36.124.247%3A5080%3Btransport%3Dudp%3Bgw%3Dopensips%3E',
        'variable_sip_req_uri': '16057819836%40sip.talkiq.net',
        'variable_sofia_profile_name': 'external',
        'variable_recovery_profile_name': 'external',
        'variable_audio_media_flow': 'sendrecv',
        'variable_rtp_use_codec_string': 'PCMU%408000h%4020i',
        'variable_rtp_audio_recv_pt': '0',
        'variable_rtp_use_codec_name': 'PCMU',
        'variable_rtp_use_codec_rate': '8000',
        'variable_rtp_use_codec_ptime': '20',
        'variable_rtp_use_codec_channels': '1',
        'variable_rtp_last_audio_codec_string': 'PCMU%408000h%4020i%401c',
        'variable_read_codec': 'PCMU',
        'variable_original_read_codec': 'PCMU',
        'variable_read_rate': '8000',
        'variable_original_read_rate': '8000',
        'variable_call_uuid': 'efc6b08d-456b-45e3-89bb-cb5679fbb744',
    })