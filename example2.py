import prefablib

input = """{
    "$id": 0,
    "$type": "0|Game.Prefabs.BuildingExtensionPrefab, Game",
    "name": "Building Extension Prefab Test",
    "active": true,
    "components": {
        "$id": 1,
        "$type": "1|System.Collections.Generic.List`1[[Game.Prefabs.ComponentBase, Game]], mscorlib",
        "$rlength": 3,
        "$rcontent": [
            {
                "$id": 2,
                "$type": "2|Game.Prefabs.ServiceUpgrade, Game",
                "name": "ServiceUpgrade",
                "active": true,
                "m_Buildings": {
                    "$id": 3,
                    "$type": "3|Game.Prefabs.BuildingPrefab[], Game",
                    "$rlength": 1,
                    "$rcontent": [
                        $fstrref:"CID:randomlettersandnumbers123"
                    ]
                },
                "m_UpgradeCost": 10000,
                "m_XPReward": 0,
                "m_MaxPlacementOffset": -1,
                "m_MaxPlacementDistance": 0
            }, 
            {
                "$id": 4,
                "$type": "4|Game.Prefabs.UIObject, Game",
                "name": "UIObject",
                "active": true,
                "m_Group": null,
                "m_Priority": 0,
                "m_Icon": "coui://customassets/abc/def/ghi.svg",
                "m_IsDebugObject": false
            }
        ]
    },
    "m_Meshes": {
        "$id": 7,
        "$type": "8|Game.Prefabs.ObjectMeshInfo[], Game",
        "$rlength": 0,
        "$rcontent": [

        ]
    },
    "m_Circular": false,
    "m_ExternalLot": false,
    "m_Position": {
        "$type": "9|Unity.Mathematics.float3, Unity.Mathematics",
        "x": 0,
        "y": 0,
        "z": 0
    },
    "m_OverrideLotSize": {
        "$type": 7,
        "x": 0,
        "y": 0
    },
    "m_OverrideHeight": 0
}"""

prefab = prefablib.reads(input)

print("INPUT:", input)

# here you can like do anything to the prefab object

print("OUTPUT:", prefablib.dumps(prefab))