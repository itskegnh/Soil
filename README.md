# Soil
Simple, Object, Interface, Language. An assembly inspired, down to earth programming language. Not built for commercial use, but as a small challenge for those bored of conventional languages. Soil provides the challenge of writing code with memory, type, value, and variable limitations. 

# Knowledge
- Soil uses a pointer system to modify memory.
- You can only modify memory, at the location your pointer is at. Unless you create a virtual pointer, which can be used to modify memory at any location.

# Instructions
| Instruction | Description | Argument(s) | Example | Reference |
| - | - | - | - | - |
| MOV | Move the pointer by amount. | Amount (INT) | `MOV -0xC1` | `0x00` |
| PNT | Move the pointer a location. | Location (INT) | `PNT 0xFF` | `0x01` |
| ADD | Add amount to the value pointed to. | Amount (INT) | `ADD 0x03` | `0x02` |
| SUB | Subtract amount from the value pointed to. | Amount (INT) | `SUB 0x03` | `0x03` |
| SET | Set the value pointed to. | Value (INT) | `SET 0x03` | `0x04` |
| MUL | Multiply the value pointed to by amount. | Amount (INT) | `MUL 0x03` | `0x05` |
| DIV | Divide the value pointed to by amount. | Amount (INT) | `DIV 0x03` | `0x06` |
| MOD | Set the value to the remainder of the value divided by amount. | Amount (INT) | `MOD 0x03` | `0x07` |
| INP | Input a number of characters. | Amount (INT) | `INP 0x03` | `0x08` |
| OUT | Output a number of characters. | Amount (INT) | `OUT 0x03` | `0x09` |
| JMP | Jump to a label. | Label (INT) | `JMP 0xFF` | `0x0A` |
| !JMP | Jump to a label, if the joined value is not the value pointed to. | Label (INT) | `!JMP 0xFF` | `0x0B` |
| LBL | Create a label with the name label | Label (INT) | `LBL 0xFF` | `0x0C` |
| JOIN | Give an instruction multiple params. (| alias) | `JMP 0x00 \| 0xFF` | `0x0D` |
| HLT | Stop the program, output error code if not 0x00. | Code (INT) | `HLT` | `0x0E` |
| EXT | Extend your program to use custom instructions. (Can be joined with the OPCODE for the instruction.) | Package (STR) | `EXT SQRT | 0x10` | `0x0F` |

## QOL Features
- You can specify a virtual pointer with `@ 0x00`. For example, to set the memory at 0x00 to 0xFF, instead of moving your pointer create a new temp virtual pointer `SET 0xFF @ 0x00`.

# Compiled.
- Unlike `|`, `@` compiles to two `PNT` instructions, one before and one after the statement.
- If the compiler finds two `PNT` instructions in a row, the first one is ignored.
- any line ending in a `:` is considered a label.