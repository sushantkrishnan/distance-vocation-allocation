import streamlit as st
import pickle
import numpy as np




def main():
	st.title("Vocational Course Allocation System")
	st.write("Build with Streamlit by Rajarshi and Sushant")
	msg=st.text_input("Enter you name")
	msg1=st.text_input("Enter you PIN code")
	option = st.selectbox("Choose a category",("Technical","Medical","SocialScience","Management","Language","Agro"))
	
	if option=="Technical":
    		option1 = st.selectbox("Choose 1st Preference",("CSE","MECH","ECE","CIV","EEE","IT"))
    		option2 = st.selectbox("Choose 2nd Preference",("CSE","MECH","ECE","CIV","EEE","IT"))
    		option3 = st.selectbox("Choose 3rd Preference",("CSE","MECH","ECE","CIV","EEE","IT"))
	

	elif option=="Medical":
    		option1 = st.selectbox("Choose 1st Preference",("Nursing","Pharmacy","Dentistry","Ayurveda","Homeopathy","Physiotherapy","Unani"))
    		option2 = st.selectbox("Choose 2nd Preference",("Nursing","Pharmacy","Dentistry","Ayurveda","Homeopathy","Physiotherapy","Unani"))
    		option2 = st.selectbox("Choose 3rd Preference",("Nursing","Pharmacy","Dentistry","Ayurveda","Homeopathy","Physiotherapy","Unani"))


	elif option=="SocialScience":
    		option1 = st.selectbox("Choose 1st Preference",("PoliticalScience ","Sociology ","History","Economics","Geography","Psychology","PublicAdministration"))
    		option2 = st.selectbox("Choose 2nd Preference",("PoliticalScience ","Sociology ","History","Economics","Geography","Psychology","PublicAdministration"))
    		option2 = st.selectbox("Choose 3rd Preference",("PoliticalScience ","Sociology ","History","Economics","Geography","Psychology","PublicAdministration"))


	elif option=="Management":
    		option1 = st.selectbox("Choose 1st Preference",("BusinessAdmin","BusinessMgmt","Marketing","Technology","Finance","HumanResource"))
    		option2 = st.selectbox("Choose 2nd Preference",("BusinessAdmin","BusinessMgmt","Marketing","Technology","Finance","HumanResource"))
    		option3 = st.selectbox("Choose 3rd Preference",("BusinessAdmin","BusinessMgmt","Marketing","Technology","Finance","HumanResource"))
    		

	elif option=="Language":
    		option1 = st.selectbox("Choose 1st Preference",("Hindi","Bengali","Urdu","Sanskrit","Tamil","Telugu","Punjabi","English","French","German","Spanish"))
    		option2 = st.selectbox("Choose 2nd Preference",("Hindi","Bengali","Urdu","Sanskrit","Tamil","Telugu","Punjabi","English","French","German","Spanish"))
    		option3 = st.selectbox("Choose 3rd Preference",("Hindi","Bengali","Urdu","Sanskrit","Tamil","Telugu","Punjabi","English","French","German","Spanish"))
    		


	elif option=="Agro":
    		option1 = st.selectbox("Choose 1st Preference",("Agriculture","Horticulture","Forestry","Sericulture","Vaterinary","Dairy"))
    		option2 = st.selectbox("Choose 2nd Preference",("Agriculture","Horticulture","Forestry","Sericulture","Vaterinary","Dairy"))
    		option3 = st.selectbox("Choose 3rd Preference",("Agriculture","Horticulture","Forestry","Sericulture","Vaterinary","Dairy"))
    				

	if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			print(option)
			
			
			if option=="Technical":
				st.success("This is Technical")

			elif option=="Medical":
    				st.success("This is Medical")
			
			elif option=="SocialScience":
    				st.success("This is Social Science")

			elif option=="Management":
    				st.success("This is Management")

			elif option=="Language":
    				st.success("This is Language")

			elif option=="Agro":
    				st.success("This is Agriculture")
			else:
				st.error("Sample Error")
				
main()
