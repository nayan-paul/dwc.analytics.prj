import traceback
import boto3
import json
#Firehose data ingestion
#pip install boto3

#M1
def sendData2Firehose():
	try:
		client = boto3.client('firehose',aws_access_key_id='AKIAIJKQWW77RESX7ZPQ',aws_secret_access_key='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',region_name='us-east-1')
		
		inputdata = { 'data': '{   "click_id": 2,   "click_pid": "vc92daf3ce1ecd4046e11ba79b634f9b675398d83",   "timestamp": "0000-00-00 00:00:00",   "event_type": 1,   "unique_click": 1,   "click_visit_pid": "",   "click_lander_id": "",   "session_id": "164d9bdb9be89b8f350de0b0388d8ecec83cb176",   "user_id": 17392,   "unique_user": 1,   "sub_id": "QHZ6CYZ12E4391603224166DLR9",   "destination_type": 1,   "destination_id": 29,   "link_position": 0,   "filter_type": 1,   "filter_id": 6,   "referral_domain": "",   "referral_link": "",   "redirect_link": "cq8f23.cqlink.net/ctdev/acfd17120fb15281b08dedb0bda9e9025?cid=smh100&debug=42r84AC4",   "redirect_destination": "http://affiliate.trk4.com/rd/r.php?sid=13510&pub=100864&c1=17&c2={tracking_id}&c3=QHZ6CYZ12E4391603224166DLR9&cid=smh100&debug=42r84AC4",   "campaign_id": 17,   "account_id": 3,   "traffic_source_id": 13,   "traffic_source_account_id": 17,   "vendor_id": 9,   "path_type": 0,   "path_id": 488,   "tsv_cid": "smh100",   "tsv_cost": "",   "tsv_1": "",   "tsv_2": "",   "tsv_3": "",   "tsv_4": "",   "tsv_5": "",   "tsv_6": "",   "tsv_7": "",   "tsv_8": "",   "tsv_9": "",   "tsv_10": "",   "ip_address": "",   "connection_id": "fae38b1127d0741416fa2a73ac8c1a8f",   "isp_carrier": "",   "mobile_carrier": false,   "connection_type": "Cable/DSL",   "country": "Philippines",   "country_code": "PH",   "state": "Unknown",   "city": "Unknown",   "device_id": "11d63eb7ff198475924e61400cf3d676",   "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",   "os": "Windows",   "os_version": 10,   "browser": "Chrome",   "browser_version": 54,   "device_category": "Desktop",   "screen_resolution": "Unknown",   "language": "en",   "mobile_brand": "Unknown",   "mobile_model": "Emulator" }'}
		
		resp = client.put_record(DeliveryStreamName="firehose_es_1", Record={'Data':json.dumps(inputdata)})
		
		print resp
	#try
	except:
		traceback.print_exc()
	#except
	finally:
		print 'End of process...'
	#finally
#M1
##############################################################################################

if __name__=='__main__':
	sendData2Firehose()
#if