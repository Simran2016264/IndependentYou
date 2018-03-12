import sys
import operator
import requests
import json
import re
import watson_developer_cloud
#from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
#from watson_developer_cloud import ConversationV1 

#conversation = ConversationV1(
#    username='244c046d-aac5-44fb-b399-e68c3adc55cd',
#   password='gnbS1GYKogC0',
#    version='2017-04-21')

#pi_username = '244c046d-aac5-44fb-b399-e68c3adc55cd'
#pi_password = 'gnbS1GYKogC0'

#conversation = Conversation(username=pi_username, password=pi_password)
#pi_result = conversation.profile(text)

conversation = watson_developer_cloud.ConversationV1(
    username='244c046d-aac5-44fb-b399-e68c3adc55cd',
    password='gnbS1GYKogC0',
    version='2018-02-16'
)

response = conversation.message(
    workspace_id='b9d8187b-da65-4de7-94b4-749f1d1f2e6e',
    input={
        'text': 'Hello'
    }
)
k = json.dumps(response, indent = 2)
k=k.split()
flag = 0
counter = 0
ss = ""
for i in k:
	if(i=="\"output\":"):
		flag = 1
	if(flag == 1):
		counter+=1
	if(counter>=5):
		if(i[len(i)-1]!='\"'):
			ss+=i+" "
		else:
			ss+=i
			break
print ss

