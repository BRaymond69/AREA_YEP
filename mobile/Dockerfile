FROM ubuntu:latest

# Init Ubuntu

ENV GRADLE_VERSION="6.8.3"
ENV GRADLE_HOME=/opt/gradle/gradle-${GRADLE_VERSION}
ENV PATH=${GRADLE_HOME}/bin:${PATH}
ENV ANDROID_HOME=/opt/android/
ENV ANDROID_SDK_ROOT=/opt/android/
ENV PATH="$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$PATH"
ENV SDKMANAGER="${ANDROID_HOME}cmdline-tools/bin/sdkmanager"

RUN apt-get update
RUN apt-get install -y curl sudo nodejs
RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN sudo apt-get update && sudo apt-get install -y yarn openjdk-11-jdk
RUN apt install -y android-sdk-*
RUN sudo apt install wget -y
RUN sudo apt install unzip -y
RUN wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -P /tmp
RUN sudo unzip -d /opt/gradle /tmp/gradle-*.zip
RUN wget https://dl.google.com/android/repository/commandlinetools-linux-6858069_latest.zip -P /tmp
RUN unzip /tmp/com* -d ${ANDROID_HOME}


# Make sure emulator path comes before tools. Had trouble on Ubuntu with emulator from /tools being loaded
# instead of the one from /emulator


RUN yes | ${SDKMANAGER} --sdk_root=${ANDROID_HOME} "tools"
RUN ${SDKMANAGER} --update --sdk_root=${ANDROID_HOME}
RUN ${SDKMANAGER} --list --sdk_root=${ANDROID_HOME}
RUN ${SDKMANAGER} "build-tools;28.0.3" "platform-tools" "platforms;android-28" "tools" --sdk_root=${ANDROID_HOME}
RUN ${SDKMANAGER} --licenses --sdk_root=${ANDROID_HOME}



# Copy files required to build
COPY . /mobile/
WORKDIR /mobile/android

# install required depedencies
RUN npm install --legacy-peer-dep

# APK Maker
CMD ["/opt/gradle/gradle-6.8.3/bin/gradle", "assembleRelease"]
