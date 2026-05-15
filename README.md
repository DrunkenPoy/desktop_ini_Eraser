# desktop.ini Eraser

Google 드라이브(File Stream) 동기화 폴더에서 자동 생성되는 `desktop.ini` 파일을 일괄 검색하여 삭제하는 Python 스크립트입니다.

## 왜 필요한가요?

Windows에서 Google 드라이브를 사용하면 각 폴더마다 `desktop.ini` 파일이 자동으로 생성됩니다. 이 파일들이 Git 저장소에 포함되면 불필요한 변경사항이 발생하여 커밋 히스토리를 오염시킵니다.

## 사용법

### 1. config.ini 설정

`config.ini` 파일에서 검색할 경로를 지정합니다.

```ini
[Settings]
repo_path = E:\.shortcut-targets-by-id\...\GitRepos
```

### 2. 실행

```bash
python Delete.py
```

실행하면 지정된 경로에서 발견된 모든 `desktop.ini` 파일 목록을 보여주고, Enter를 누르면 삭제가 진행됩니다.

### 3. GitHub Desktop과 함께 사용 (선택)

`CustomGitOpen.bat`을 실행하면 `desktop.ini` 정리 후 자동으로 GitHub Desktop이 열립니다.

## PyInstaller로 exe 빌드

```bash
pip install pyinstaller
pyinstaller --onefile Delete.py
```

빌드된 exe 파일과 같은 폴더에 `config.ini`를 함께 두면 됩니다.

## 라이선스

[MIT License](LICENSE)