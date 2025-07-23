import prefablib

prefab = prefablib.BuildingExtensionPrefab("Cargo Upgrade Coal")

prefab.components.append(
    prefablib.ServiceUpgrade(
        buildings=[prefablib.CID("gh3q4gh4qng43nu7gn")],
        upgrade_cost=10000,
        xp_reward=0,
        max_placement_offset=-1,
        max_placement_distance=0
        )
)
prefab.components.append(
    prefablib.UIObject(
        group=prefablib.GUID("gh8u4gnuegu4wegun"),
        priority=0,
        icon="sh/it",
        isdebug=False
        )
)
prefab.meshes.append(
    prefablib.Mesh(
        prefablib.GUID("abc123")
    )
)

data = prefablib.dumps(prefab)

print(data)