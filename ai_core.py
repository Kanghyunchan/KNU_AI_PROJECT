import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def review_code_logic(code_content):
    try:
        llm = ChatOpenAI(
            model="gpt-5-mini", 
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.2
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 10년 경력의 시니어 백엔드 개발자입니다. 
다음 코드를 [버그, 스타일, 보안, 성능] 4가지 관점에서 리뷰하고 한국어로 리포트를 작성하세요.
각 항목별로 문제점과 개선된 코드 예시를 반드시 포함해야 합니다."""),
            ("user", "리뷰할 코드는 다음과 같습니다:\n\n{code}")
        ])

        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"code": code_content})

    except Exception as e:
        return f"분석 중 에러가 발생했습니다: {e}"