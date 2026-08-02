# How to turn this into an Android APK

This project is a Flask web app. To make a real APK you wrap it with **Capacitor**.

### Requirements on your computer
- Node.js (https://nodejs.org)
- Android Studio (https://developer.android.com/studio)  
  (or at least the Android SDK + command line tools)

### Steps (copy-paste friendly)

1. Clone / go into the project:
```bash
cd cyber-red-localhost-terminal
```

2. Install Capacitor:
```bash
npm init -y
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init "Cyber Red Terminal" "com.cyberred.terminal" --web-dir=templates
```

3. Add Android platform:
```bash
npx cap add android
```

4. Because this is a Flask backend (not pure static files), the easiest ways are:

**Option A – Simple (recommended for most people)**  
Just use the PWA version (already set up). On your phone open the site in Chrome → menu → “Add to Home screen”. It installs like an app and works great.

**Option B – Real APK with local server**  
You need the Flask server running on the same machine/network, then point Capacitor to it, or convert the frontend to pure static and run commands differently. Full local terminal inside a pure APK is limited on Android without root.

### Easiest path right now
1. Run the Python app:
```bash
pip install -r requirements.txt
python app.py
```

2. On your Android phone open `http://YOUR-COMPUTER-IP:5000` in Chrome

3. Tap the three dots → **Install app** / **Add to Home screen**

You now have a glowing red cyber terminal icon on your phone.

---

If you want a fully offline native APK with limited terminal features, reply and I can restructure the project further.
