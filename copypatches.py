import pathlib
import tomllib

cwd = pathlib.Path.cwd() / 'game'

for dir in (cwd / 'Mods').iterdir():
    for (c, dirs, files) in dir.walk():
        for file in files:
            if file.endswith('.toml'):
                file_path = c / file
                toml = tomllib.loads(file_path.read_text())
                if 'patches' not in toml: continue
                for patch_root in toml['patches']:
                    if 'module' not in patch_root: continue
                    patch = patch_root['module']
                    print(patch)
                    source_file = dir / patch['source']
                    out_file = cwd / (patch['name'].replace('.', '/') + '.lua')
                    out_file.parent.mkdir(exist_ok=True)
                    out_file.write_text(source_file.read_text())