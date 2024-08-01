# Auto Attendance System Setup on Raspberry Pi

This guide will help you set up the Auto Attendance System on a Raspberry Pi. Follow the steps below to clone the repository, install the necessary requirements, and run the system.

## Prerequisites

- Raspberry Pi with an operating system installed.
- SSH access to the Raspberry Pi.
- Python and pip installed.

## Setup Instructions

1. **SSH into the Raspberry Pi**

    Open your terminal and SSH into your Raspberry Pi using the following command:

    ```bash
    ssh pi@<your_raspberry_pi_ip_address>
    ```

    Replace `<your_raspberry_pi_ip_address>` with the actual IP address of your Raspberry Pi.

2. **Clone the Repository**

    Once you are logged into the Raspberry Pi, clone the Auto Attendance repository:

    ```bash
    git clone https://github.com/thesanju/Auto-Attendance.git
    ```

3. **Navigate to the Project Directory**

    Change your current directory to the Auto-Attendance project directory:

    ```bash
    cd Auto-Attendance
    ```

4. **Install the Requirements**

    Install the required Python packages by running:

    ```bash
    pip install -r requirements.txt
    ```

5. **Add Faces for Attendance**

    To add faces to the attendance system, run the following script:

    ```bash
    python add_faces.py
    ```

    Follow the on-screen instructions to add faces.

6. **Test the System**

    To test the system, run:

    ```bash
    python test.py
    ```

7. **Run the Web Interface**

    To start the web interface, use Streamlit:

    ```bash
    streamlit run app.py
    ```

## Conclusion

By following these steps, you should have the Auto Attendance System up and running on your Raspberry Pi. If you encounter any issues, please refer to the repository's issue tracker for support.

