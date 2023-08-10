# Building Qt for iOS

~~~bash
../../qt6/qtbase/configure -developer-build -platform macx-ios-clang -qt-host-path ../qt6-dev-build/qtbase -sdk iphoneos -nomake examples -nomake tests
~~~