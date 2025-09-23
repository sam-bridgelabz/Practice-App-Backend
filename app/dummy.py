from app.config.database import SessionLocal
from app.models.ques_model import Programme, Module, Topic, Subtopic, Question
import uuid, json
from sqlalchemy.sql import func

db = SessionLocal()

# create programme
prog = Programme(id=str(uuid.uuid4()), name="Full-Stack Development")
db.add(prog); db.commit()

# module
mod = Module(id=str(uuid.uuid4()), name="Backend APIs", programme_id=prog.id)
db.add(mod); db.commit()

# topic
top = Topic(id=str(uuid.uuid4()), name="FastAPI", module_id=mod.id)
db.add(top); db.commit()

# subtopic
sub = Subtopic(id=str(uuid.uuid4()), name="Routing", topic_id=top.id)
db.add(sub); db.commit()

# 1️⃣ Fetch existing hierarchy IDs (take the first record of each)
prog = db.query(Programme).first()
mod  = db.query(Module).filter_by(programme_id=prog.id).first()
top  = db.query(Topic).filter_by(module_id=mod.id).first()
sub  = db.query(Subtopic).filter_by(topic_id=top.id).first()

# 2️⃣ Prepare 5 dummy questions
questions = []
for i in range(1, 6):
    q = Question(
        id=str(uuid.uuid4()),
        programme_id=prog.id,
        module_id=mod.id,
        topic_id=top.id,
        subtopic_id=sub.id,
        question_type="SELF",
        answer_type="MCQ",
        difficulty="MEDIUM",
        stem_md=f"Sample question {i}: What is FastAPI used for?",
        solution_md="FastAPI is used to build APIs quickly with Python.",
        score_weight=1.0,
        metadata_json=json.dumps({"tags": ["fastapi", "api"], "index": i}),
        version=1,
        is_current=1,
    )
    questions.append(q)

# 3️⃣ Bulk insert
db.add_all(questions)
db.commit()
db.close()

print("5 dummy questions inserted.")



db.close()
print("Dummy data inserted.")
