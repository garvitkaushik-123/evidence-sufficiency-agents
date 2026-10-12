# Related work notes

Written after reading the full text of Joren et al. (2025) and the method sections of the other papers (PDFs from arXiv). Everything stated about a paper below was read in that paper; where a detail could not be confirmed it is marked **unverified**. Paraphrased, not quoted. Please spot-check the section pointers before the report goes out.

## 1. The closest paper: Sufficient Context (Joren et al., ICLR 2025)

What it does (Sec. 1, 3, 4, 5):
- **Definition (Sec. 3.1).** A (question, context) pair has sufficient context if some plausible answer to the question can be derived from the context. It needs no ground-truth answer, and the context may even support a wrong answer. For multi-hop questions the model may combine facts that are in the context but must not assume connections that are not (Remark 1).
- **Labels (Sec. 3.2).** An LLM autorater (Gemini 1.5 Pro, one-shot) reaches 93% accuracy on 115 human-labelled instances drawn from PopQA, FreshQA, Natural Questions and EntityQuestions (not HotpotQA or MuSiQue). A cheap baseline, "the ground-truth answer string appears in the context", gets accuracy 0.81, precision 0.87, recall 0.76 on the same set (Table 1).
- **Analysis (Sec. 4).** On FreshQA, MuSiQue-Ans and HotpotQA (500 random dev questions for the last two) they stratify model answers into correct, abstain and hallucinate by sufficiency. The context is fixed per question (MuSiQue: its 20 provided snippets; HotpotQA: top-5 retrieved). About 45% of MuSiQue and about 46% of HotpotQA contexts are sufficient (read off their Fig. 1 and 2). Models often answer instead of abstaining when context is insufficient, and strong models answer correctly 35 to 62% of the time with insufficient context (contribution 2). They explain this with a taxonomy (Table 2): yes/no guesses, multi-hop fragments completed from memory, ambiguous queries, closed-book knowledge, rater errors.
- **Selective generation (Sec. 5.1).** A logistic regression on the binary sufficiency label (from the smaller FLAMe autorater) plus the model's self-rated confidence (P(Correct) or P(True)) decides whether to answer or abstain; it improves the share of correct answers among answered questions by 2 to 10%.
- **Stated limitation (Sec. 6).** They note the autorater could be used iteratively to decide whether to retrieve more or answer, and leave this untested.

How this project differs:
1. **Who judges.** They use an external autorater on a fixed context. We use the answering model's own verdict, inside a loop, at every one of five steps, and score it against objective labels (gold paragraphs, answer text in context).
2. **The decision.** They choose between answering and abstaining. We choose between retrieving more and stopping, and measure the cost (steps) against accuracy.
3. **The context moves.** Our evidence grows step by step with BM25 over a pooled corpus, so we observe how often a verdict flips and how much accuracy later steps add.

Where results line up (not independent confirmation, different setups):
- Correct answers without full evidence are common. Our error analysis found about 7 in 10 gold-coverage "premature stops" were already answerable from the retrieved text, and our taxonomy mirrors their Table 2 (parametric completion, ambiguous question).
- Our second sufficiency label is their "contains the ground truth" baseline. Their numbers say it is reasonable but imperfect (precision 0.87, recall 0.76 against humans), so we report it next to gold coverage and say the truth lies between them.
- They use a continuous confidence (P(Correct), the probability the answer is right) as one of two signals. Our judge asks for the probability that the evidence suffices, and the small Gemini model answers exactly 0 or 1 in 93 to 94% of judgements while the strong model's probabilities are less extreme (61% and 25% exactly 0 or 1 on HotpotQA and MuSiQue, 91% and 75% within 0.1 of an extreme). Different quantity, so do not claim a contradiction.

## 2. Other papers

| Paper | What it does | How it stops or decides | Relation to this work |
|---|---|---|---|
| IRCoT (Trivedi et al., ACL 2023) | Alternates one chain-of-thought sentence and one retrieval of K paragraphs, using the last sentence as the query. Tested on HotpotQA, 2WikiMultihopQA, MuSiQue, IIRC. | Stops when the generated reasoning contains the final-answer phrase or a step cap is hit (8 in their experiments). | Stopping is a by-product of answering, with no separate sufficiency estimate. We pull the decision out and compare rules. |
| FLARE (Jiang et al., EMNLP 2023) | Predicts the next sentence and retrieves only if it contains a token below a probability threshold. | Retrieval is triggered by token-level confidence (threshold theta). They report accuracy plateaus once retrieval is used on about 60% of sentences on 2WikiMultihopQA. | Closest in spirit to a threshold rule. Theirs uses token probabilities, ours a verbalised probability. Their plateau is consistent with ours (more steps stop helping), different task. |
| Self-RAG (Asai et al., 2023) | Fine-tunes a model to emit reflection tokens (retrieve, relevance, support, usefulness) that decide when to retrieve and critique passages and outputs. | Learned: the model predicts a retrieve token. | Trained self-assessment. We test whether prompted self-judgement is calibrated, with no training. Venue **unverified** (the PDF I read is labelled preprint). |
| Adaptive-RAG (Jeong et al., NAACL 2024) | A small classifier picks no retrieval, single-step or iterative retrieval per question by predicted complexity. | Routes before retrieval, labels collected automatically from model outcomes and dataset biases. | Decides how much to retrieve up front. We decide when to stop during retrieval. |
| AgentRewardBench (Lu et al., 2025) | 1,302 expert-annotated web-agent trajectories across 5 benchmarks and 4 LLMs; compares 12 LLM judges and rule-based checks. | n/a (evaluates judges). | Motivates validating an LLM judge of agent progress against expert labels. They find no judge best everywhere and rule-based checks understate success. Web agents, not retrieval, so cite only for the judge-validation point. |

## 3. Draft Related Work paragraph (for the report, about 330 words)

Retrieval-augmented generation (RAG) has been studied for when to retrieve and for whether retrieved context suffices. Several methods decide during generation when more evidence is needed. IRCoT interleaves retrieval with chain-of-thought sentences and ends when the reasoning produces an answer or a step budget runs out (Trivedi et al., 2023). FLARE retrieves when the model's next sentence contains low-probability tokens (Jiang et al., 2023), and Self-RAG trains a model to emit reflection tokens that decide when to retrieve and critique what it retrieved (Asai et al., 2023). Adaptive-RAG instead routes each question to no, single-step or iterative retrieval with a trained complexity classifier (Jeong et al., 2024). In these systems the decision to stop is either implicit in answering or learned jointly with the model; none of them, in the papers we read, isolates the stopping decision and compares simple rules on the same logged trajectories.

The closest work asks whether the retrieved context is sufficient. Joren et al. (2025) define sufficient context as context from which a plausible answer to the question can be derived, label it with an LLM autorater, and show that models often answer instead of abstaining when context is insufficient, and that they are also correct on a sizeable share of questions with insufficient context. They combine the sufficiency label with self-reported confidence for selective answering, and note in their limitations that the autorater could be used to decide whether to retrieve more, which they do not try. We study that setting: the answering model judges its own evidence after every retrieval step in a five-step loop, and we score the verdicts against two objective labels (all gold supporting paragraphs retrieved, and the gold answer present in the evidence), then compare stopping rules by accuracy against retrieval steps. Because our verdict comes from the answering model rather than a separate autorater, our results also bear on how far self-assessment can be trusted. This echoes the concern, studied for web agents by AgentRewardBench, that LLM judges need validating against expert labels (Lu et al., 2025).

## 4. What we can and cannot claim

Can claim (supported by what we read and what we measured):
- We evaluate the answering model's own sufficiency judgement inside a multi-step loop against two objective labels, and compare stopping rules (fixed, self-judge, threshold, oracle) from one set of logs.
- We extend the question left open in the limitations of Joren et al. (2025) to the retrieval-stopping setting, with BM25 on pooled corpora, two datasets, two Gemini models.

Cannot claim:
- That no one has studied stopping or sufficiency in agents. We read six papers and did not search further. Say "as far as we found".
- That our verdict matches or beats their autorater. Different judge, different labels, different contexts.
- Anything about other model families, open-domain corpora, or dense retrieval (not run yet).

## 5. Left unverified

- Venue of Self-RAG (I believe a conference version exists; the arXiv PDF says preprint).
- Exact values read off their figures (the 46% HotpotQA sufficiency rate comes from a bar chart label order, the 55.4% insufficient MuSiQue figure is in the Fig. 1 caption).
- Dataset and BM25 bib entries in `refs.bib` were written from memory.
- I did not read the appendices of Joren et al. (autorater prompts, extra datasets), nor the experiment sections of Self-RAG, FLARE and Adaptive-RAG.
