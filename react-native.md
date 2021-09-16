<!-- Pasos preliminares -->

$ choco install -y nodejs.install python2 jdk8
$npm install -g react-native-cli

<!-- fin pasos -->

$ npx react-native init nombreDelProyecto 
$ npx react-native run-android

<!-- Instalar modulos externos -->

npm install --save react-native-video
npm install
react-native link react-native-video = con el comando link crea el puente entre js and java

<!-- Borrar cache -->

npm start --reset-cache

<!-- dependencia para cache reeact-redux -->

npm install --save redux-persist
npm cache clean -f

<!--  -->
<!-- react native navigation -->

npm install react-navigation --save

<!-- react native gesture handler -->

npm install --save react-native-gesture-handler

<!-- react navigation stack -->

npm install --save react-navigation-stack

<!-- react navigation todo junto -->

npm install @react-navigation/native @react-navigation/stack
npm install react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view

npm install @react-navigation/bottom-tabs <!-- react native tabs -->

npm install react-native-picker-select <!-- instalar un select ->
