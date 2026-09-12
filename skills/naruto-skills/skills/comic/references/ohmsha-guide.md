# Ohmsha Manga Guide Style

Guidelines for `--style ohmsha` educational manga comics.

## Character Setup

| Role | Default | Traits |
|------|---------|--------|
| Student (Role A) | Nobita | Confused, asks basic but crucial questions, represents reader |
| Mentor (Role B) | Doraemon | Knowledgeable, patient, uses gadgets as technical metaphors |
| Antagonist (Role C, optional) | Gian | Represents misunderstanding, or "noise" in the data |

Custom characters: `--characters "Student:Alex,Mentor:Professor,Antagonist:BugMonster"`

## Character Reference Sheet Style

For Ohmsha style, use manga/anime style with:
- Exaggerated expressions for educational clarity
- Simple, distinctive silhouettes
- Bright, saturated color palettes
- Chibi/SD (super-deformed) variants for comedic reactions

## Outline Spec Block

Every ohmsha outline must start with:

```markdown
COMIC SPECIFICATION
- Language: [Same as input content]
- Style: Ohmsha (Manga Guide), Full Color
- Layout: Vertical Scrolling Comic
- Characters: [List character names and roles]
- Character Reference: characters/characters.png
- Page Limit: ≤20 pages
```

## Visual Metaphor Rules (Critical)

**NEVER** create "talking heads" panels. Every technical concept must become:

1. **A tangible gadget/prop** - Something characters can hold, use, demonstrate
2. **An action scene** - Characters doing something that illustrates the concept
3. **A visual environment** - Stepping into a metaphorical space

### Examples

| Concept | Bad (Talking Heads) | Good (Visual Metaphor) |
|---------|---------------------|------------------------|
| Word embeddings | Characters discussing vectors | Doraemon reveals a "word-vector compressor" that turns books into colored spheres |
| Gradient descent | Explaining math formula | Nobita rolls a ball through a valley to find its lowest point |
| Neural network | Diagram on whiteboard | The characters enter a glowing maze made of connected nodes |

## Page Title Convention

Avoid AI-style "Title: Subtitle" format. Use narrative descriptions:

- ❌ "Page 3: Introduction to Neural Networks"
- ✓ "Page 3: Nobita is overwhelmed by a flood of words, and Doraemon reveals the word-vector compressor"

## Ending Requirements

- NO generic endings ("What will you choose?", "Thanks for reading")
- End with: Technical summary moment OR character achieving a small goal
- Final panel: Sense of accomplishment, not open-ended question

### Good Endings

- Student successfully applies learned concept
- Visual callback to opening problem, now solved
- Mentor gives summary while student demonstrates understanding

### Bad Endings

- "What do you think?" open questions
- "Thanks for reading this tutorial"
- Cliffhanger without resolution

## Layout Preference

Ohmsha style typically uses:
- `webtoon` (vertical scrolling) - Primary choice
- `dense` - For information-heavy sections
- `mixed` - For varied pacing

Avoid `cinematic` and `splash` for educational content.
