[繁體中文](README.md)｜[简体中文](README.zh-CN.md)｜[English](README.en.md)

# Dan Koe HUMAN 3.0 prompts: community revisions in English and Chinese

Paste a prompt into an AI conversation to reflect on your experiences across Mind, Body, Spirit, and Vocation, then review the AI's tentative observations and suggested next step.

This community project organizes and revises material from Dan Koe's [HUMAN 3.0 Self-Discovery & Metatype Test](https://letters.thedankoe.com/p/prompt-human-30-self-discovery-and). It is not an official edition.

For guided self-reflection, start with a community revision below. To read or compare Dan Koe's original, see [Study the original](#research).

## Use the community revision

Choose a language and open its prompt. You do not need to install software, Python, or run tests.

| Language and prompt | Body starts with | Final paragraph starts with (copy the whole paragraph) |
|---|---|---|
| [繁體中文](PROMPT_TW.md) | `你是一位直接且尊重使用者的自我反思訪談引導者` | `"成為多維度強化的自己` |
| [简体中文](PROMPT_CN.md) | `你是一位直接且尊重使用者的自我反思访谈引导者` | `"成为多维度强化的自己` |
| [English](PROMPT.md) | `You are a direct, respectful self-reflection interview guide` | `"Become multidimensionally jacked` |

1. Skip the source note at the top of the file. Copy continuously from the opening role paragraph shown in the table through the end of the final quotation, including everything in between.
2. Choose an AI service you trust and review its privacy settings. Paste the body into a new conversation and send it.
3. Wait for the AI to start asking questions, then answer in turn, sharing only what you choose. You can skip any question, pause, or stop the interview.
4. Review the short summary first and correct inaccuracies. Then choose a full report, selected sections, or the summary alone. Once you confirm and choose the scope, the AI should produce it directly.
5. The revised prompts default to one small, reversible experiment with a review condition. Extra tasks or longer plans are included only when you request them and your answers support them.

The `<!-- prompt-parity:… -->` comments are maintenance markers. You can copy them with the body without deleting them individually; they are not steps to perform. This does not guarantee that every AI service ignores them.

For examples of the revised prompts' output, see the [synthetic report](docs/RESULTS.md) or [brief summary](docs/RESULTS_EASY.md), both in Traditional Chinese. The people and answers are fictional; these are not evidence of actual results.

<a id="research"></a>
## Study the original

| Material to read or compare | Link |
|---|---|
| The original published by Dan Koe | [Author's article](https://letters.thedankoe.com/p/prompt-human-30-self-discovery-and) |
| English source reference checked against the article | [ORIGINAL.md](reference/ORIGINAL.md) |
| Unofficial faithful Traditional Chinese translation of that reference | [TRANSLATION_TW.md](reference/TRANSLATION_TW.md) |

The three prompt files in the repository root are unofficial community revisions. The English reference and faithful Traditional Chinese translation are kept separately in `reference/`, preserving the source's rules for comparison. See the [provenance notes](reference/README.md), mainly in Traditional Chinese, for the source, check date, fingerprints, and translation notes. The English reference is not a publication-day HTML archive.

The framework keeps Dan Koe's name, HUMAN 3.0; this project identifies its revisions by Git commits rather than assigning an official framework version number. The Simplified Chinese community revision was converted from the Traditional Chinese revision and reviewed; it is not a translation of the original.

To paste a reference file into a conversation, copy only the body between `<!-- reference-body:start -->` and `<!-- reference-body:end -->`, excluding the markers and notes outside the body. The original has different rules; the summary-confirmation flow described above applies only to the community revision.

## Before you use it

This is for adults who want to reflect on their experiences. It is not an empirically validated psychological test, research scale, or diagnosis. The AI's levels, types, suggested causes, and advice may be wrong or incomplete. If you use it to support coaching, education, or helping conversations, do not treat its output as a diagnosis or professional judgment about another person.

- Avoid names, addresses, account details, medical records, financial information, legal documents, and private information about others. Storage, use, and sharing depend on the AI service and your account settings. This project cannot guarantee that the service keeps your information confidential or deletes it.
- Framework levels cannot determine whether high-risk actions are suitable or safe for an individual. Do not use them to decide whether to take psychedelics, PEDs or anabolic steroids, or deliberately create financial hardship. Consult a qualified healthcare professional about health or substance use, and seek appropriately qualified, independent advice for major financial, employment, or legal decisions.
- Stop if the conversation makes you uncomfortable. For urgent physical or mental safety concerns, contact local emergency services or a qualified professional.

## Sources, revisions, and maintenance

The [changelog](CHANGELOG.md) records changes already made. The [bilingual rules comparison](docs/PROMPT_RULES.md) supports review of the revised prompts. The [provenance notes](reference/README.md) document the English reference and its Traditional Chinese translation. The [source-versus-revision comparison](docs/REVISION_COMPARISON.md) records the reasons, trade-offs, source passages, and unproven effects of each major change. Editorial and workflow changes do not establish greater psychological accuracy, scientific validation, or the author's endorsement. These local reference documents are mainly in Traditional Chinese.

Maintainers can find a manual review checklist, optional section checks, and a separate personal Git sync tool in the [maintenance guide](docs/MAINTENANCE.md), in Traditional Chinese. Readers do not need to run these tools. Tests cover tool behavior; they do not establish that a model follows the prompt or that the assessment is valid. External-model conversation acceptance checks have not yet been run.
