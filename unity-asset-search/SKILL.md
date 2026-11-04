---
name: unity-asset-search
description: Find Unity package or asset folders on GitHub by searching for a known file name, then download the matching repository subdirectory with the user's github-subdir-download.sh script.
metadata:
  short-description: GitHub에서 Unity 에셋 찾기
---

# Unity GitHub 에셋 찾기

사용자가 Unity 에셋이나 패키지의 파일명을 알고 있고, GitHub 저장소에서 해당 파일이 포함된 폴더를 찾아 내려받으려 할 때 사용한다.

## 절차

1. 파일명(예: `JungleHubWindow.cs`)을 GitHub의 **Code** 검색에서 따옴표로 감싸 검색한다. 로그인이 필요하거나 결과가 보이지 않으면 그 사실을 알리고 이용 가능한 근거로 계속 찾는다.
2. 결과의 파일 경로와 저장소를 확인한다. 대상 파일이 속한 Unity 패키지/에셋 폴더 경계를 찾아 그 폴더 전체를 받는다. 여러 경로면 주변 파일 구조와 README/package 메타데이터로 후보를 판단한다. 확정할 수 없으면 사용자에게 선택을 요청한다.
3. 검색 결과 링크에서 `https://github.com/<owner>/<repo>/tree/<ref>/<folder-path>` 형식의 폴더 URL을 만든다. `/blob/` 파일 링크를 그대로 사용하지 않는다. ref는 검색 결과에 표시된 값을 유지하며 URL 인코딩은 스크립트에 맡긴다.
4. `C:\Users\admin\Documents\Personal\github-subdir-download.sh`를 사용 가능한 bash 환경에서 실행하고, 첫 인자로 폴더 URL을 전달한다. 선택적으로 두 번째 인자로 출력 경로를 지정한다. 생략하면 현재 디렉터리에 폴더명으로 출력한다.
5. 실행 전에 출력 경로를 확인한다. 경로가 이미 있으면 덮어쓰지 말고 다른 경로를 사용한다. 완료 후 다운로드 경로와 원본 GitHub 폴더 링크를 알린다. 실패하면 오류와 git/python3 등 요구 환경을 점검한다.

저장소 전체가 아니라 Unity 패키지/에셋 하위 폴더만 받는다. 에셋을 프로젝트에 설치·복사·병합하거나 라이선스 적합성을 판단하는 작업은 사용자가 별도로 요청한 경우에만 한다.
