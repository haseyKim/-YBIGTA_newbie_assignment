
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if ! command -v conda &> /dev/null
then
    echo "[INFO] Miniconda가 설치되어 있지 않습니다. 설치를 시작합니다."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p "$HOME/miniconda3"
    "$HOME/miniconda3/bin/conda" init "$(basename "$SHELL")"
    source "$HOME/.bashrc" || source "$HOME/.zshrc" || echo "쉘 초기화 실패"
    echo "[INFO] Miniconda 설치 완료"
else
    echo "[INFO] Miniconda가 이미 설치되어 있습니다."
fi


# Conda 환셩 생성 및 활성화
## TODO
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda env remove --name myenv -y &> /dev/null
conda create --name myenv python=3.12.7 -y
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
pip install mypy

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    problem_name="${file%.py}"
    problem_number=$(echo "$problem_name" | grep -o '[0-9]\+')
    input_file="../input/${problem_name}_input"
    output_file="../output/${problem_number}_output"
    python "$file" < "$input_file" > "$output_file"

done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy . > ../mypy_log.txt 2>&1

# conda.yml 파일 생성
## TODO
conda env export --no-builds > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate