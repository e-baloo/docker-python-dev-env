FROM python:3.13

# Install system dependencies for Pygame
# These are common dependencies required for Pygame to work on Linux
RUN apt-get update && apt-get install -y \
    python3-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libportmidi-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Configure bash prompt with colors and git branch
RUN echo 'parse_git_branch() {' >> /root/.bashrc && \
    printf "%s\n" '    git branch 2> /dev/null | sed -e "/^[^*]/d" -e "s/^\* \(.*\)/ (\1)/"' >> /root/.bashrc && \
    echo '}' >> /root/.bashrc && \
    echo 'export PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\]\$(parse_git_branch)\[\033[00m\]\$ "' >> /root/.bashrc && \
    echo "alias ls='ls --color=auto'" >> /root/.bashrc && \
    echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

