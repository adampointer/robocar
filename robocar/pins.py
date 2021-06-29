from adafruit_blinka.microcontroller.tegra.t210.pin import Pin

# LHS Motors
PWM_PIN_1 = Pin("LCD_BL_PW")  # 32
MOTOR1_DIRECTION_PIN_1 = Pin("UART2_CTS")  # 36
MOTOR1_DIRECTION_PIN_2 = Pin("DAP4_DIN")  # 38

# RHS Motors
PWM_PIN_2 = Pin("GPIO_PE6")  # 33
MOTOR2_DIRECTION_PIN_1 = Pin("DAP4_FS")  # 35
MOTOR2_DIRECTION_PIN_2 = Pin("SPI2_MOSI")  # 37

# Sonar
SONAR_TRIGGER_PIN = Pin("AUD_MCLK")  # 7
SONAR_ECHO_PIN = Pin("UART2_RTS")  # 11
