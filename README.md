# 5조 팜스토리 스마트팜 Node-red
# Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard
## 구성원: 오상우, 윤현호, 박세린, 이병현, 권용만

### 개요
<p>
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/1ced2b98-ab9b-4bbd-9a42-1e828f79dffd">
</p>
<br/><br/>
Node-red 대시보드 ui에 조도센서측정기능을 추가하였습니다.(오류)<br/>
라즈베리파이와 아두이노 연동시 아두이노 UNO의 포트인 /dev/ttyACM0 이 라즈비안OS 리눅스환경에서 권한이 거부되었습니다.<br/>
<p>
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/7657eb8a-e982-4374-927c-49e9fcd162f4">
</p>
아두이노 uno에 연결된 조도센서는 라즈베리파이에서는 값을 확인하지 못하게 되었습니다...<br/>
추후에 ADC컨버터 MCP3008을 사용하여 라즈베리파이 임베디드시스템에서 동작하도록 개선하겠습니다. <br/>

### 블록도
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/ae026275-5de2-43a5-ab3d-6c16fa583b7c">
</p>

### Node-red FLOW 흐름도
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/932ba7f0-2919-44d8-a93d-09ece5f697ca">
</p>

### dashboard
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/7e1b3759-8258-455f-acd7-26ec2a7bb44b">
</p>
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/abc27d41-8cc1-4974-aec7-0aabd5d72b1a">
</p>

### 사용한 재료들
라즈베리파이4 B .ver 임베디드시스템, DHT11 센서, LED 2개, Ras pi용 Camera<br/>
Arduino Uno, 조도센서, 수분감지센서(토양)

### GPIO 세팅 및 아두이노(임시)
Raspi 4<br/>
DHT11 - Vcc: 4_pin 5V / Data: 7_pin (GPIO_4) / Ground: 6_pin<br/>
LED_Yel - 11_pin (GPIO_17) / Ground: 9_pin<br/>
LED_Red - 12_pin (GPIO_18) / Ground: 14_pin<br/>
Camera - 카메라용 케이블 소켓<br/>
<br/>
Arduino Uno /dev/ttyACM0 (임시)<br/>
조도센서 - Vcc: Power 5V pin / Out: Analog 0 pin / Ground: Power GND pin<br/>
수분감지센서(토양) - Vcc: Power 3.3V pin / Out: Analog 1 pin / Ground: Power GND pin
<br/>

### 사용한 SW요소들
Rasberry Pi OS Legacy, Nord-red 프레임워크 개발도구, dashboard 라이브러리<br/>
Arduino 보드- Uno 포트 - /dev/ttyACM0, Arduino 1. 8. 19 ver, StandardFirmata 라이브러리 (임시)
<br/>

### 구현 영상
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/91432796-efce-4379-813d-2c7d676ca6e5">
</p>
https://www.youtube.com/watch?v=134TiywJLuI
