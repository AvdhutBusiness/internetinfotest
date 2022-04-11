from pytz import country_names
from streamlit_option_menu import option_menu
import streamlit as st
from PIL import Image
import speedtest
import time


st.set_page_config(
     page_title="|| Internet SpeedTest 🧿 ||")
try:
    net = speedtest.Speedtest()
except:
    st.error("ConfigRetrievalError")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# {'{:.2f}'.format(test.upload()/1024/1024)} Mb/s"

with st.sidebar:
    choose = option_menu("More",["Internet SpeedTest","Internet Service Provider","Contact"],styles={"nav-link-selected": {"background-color": "#4F8BF9"},"--hover-color": "#4F8BF9"},icons=["speedometer","info circle","person"])


if choose == "Internet SpeedTest":
    
    image = Image.open('spe2.png')
    st.image(image=image,width=600,use_column_width=200,clamp=True)
    j = st.button("Start Test")
    if j == True:
        
        
        try:
            col1, col2, col3 = st.columns(3)
            with st.spinner("Checking Upload Speed"):
                col1.metric("Upload Speed",f"{'{:.2f}'.format(net.upload()/1024/1024)} MB/S" )
            with st.spinner("Checking Download Speed"):
                col2.metric("Download Speed",f"{'{:.2f}'.format(net.download()/1024/1024)} MB/S" )
            with st.spinner("Pinging ....."):
                time.sleep(3)
                col3.metric("Ping",f"{net.results.ping} MS")
            st.success('Done!')
        except:
            st.warning("Unable to connect to servers")

if choose == "Internet Service Provider":
    info = st.button("Get Info")
    if info == True:
        try:
            with st.spinner("Fetching....."):
                ip = (net.get_config()["client"]["ip"])
                st.write(f"IP : {ip}")
                isp = net.get_config()["client"]["isp"]
                st.write(f"Internet Service Provider : {isp}")
                lat = net.get_config()["client"]["lat"]
                lon = net.get_config()["client"]["lon"]
                st.write(f"Latitude : {lat}")
                st.write(f"Longitude : {lon}")
                country = net.get_config()["client"]["country"]
                st.write(f"Country : {country_names.get(country)}")
            with st.spinner("It may take while"):
                    best_lat = net.get_best_server()["lat"]
                    best_lon = net.get_best_server()["lon"]
                    best_sponsor = net.get_best_server()["sponsor"]              
                    st.write(f"Best server : a)latitude : {best_lat }  b)longitude : {best_lon }  c)Sponsor : {best_sponsor}")
                    threads = net.get_config()["threads"]
                    st.write(f"Threads : {threads}")
            st.success("Fetching Successfull !")
            
        except:
            st.warning("Fetching failed")

if choose == "Contact":
    st.header("Contact me")
    st.write("Dear user, Thank you for visiting site . If you have any complaints or queries , then please contact me via email")
    with st.echo():
        email = "avdhutpujari.businessenenquiry@gmail.com"
    st.write("Thank You ! 😁")

