// Deterministic cosmic garden artwork for coolest-art-01.
import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(out, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(out, 'entry.png'));
