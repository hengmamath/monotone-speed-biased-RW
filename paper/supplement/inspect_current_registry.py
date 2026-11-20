"""Validate packaged source identities and the DAG; not a mathematics verifier."""
from pathlib import Path
import json
import hashlib

project = Path(__file__).resolve().parent.parent
registry = json.loads((project / 'supplement/current_route_results_and_dependencies.json').read_text())
nodes = {node['id']: node for node in registry['nodes']}
assert len(nodes) == 45
seen = set()
for node_id in registry['topological_order']:
    assert node_id in nodes
    assert set(nodes[node_id]['inputs']) <= seen
    seen.add(node_id)
assert seen == set(nodes)
checked = set()
for row in registry['selected_source_material'] + registry['historical_generation_programs_and_data']:
    path = project / row['package_path']
    content = path.read_bytes()
    assert len(content) == row['size_bytes'], path
    assert hashlib.sha256(content).hexdigest() == row['sha256'], path
    checked.add(str(path.relative_to(project)))
assert registry['unresolved_literal_program_references'] == []
print(f'Checked {len(checked)} packaged identities and the 45-node dependency order.')
print('No regional coefficient/sign proof has been validated by this identity/DAG check.')
