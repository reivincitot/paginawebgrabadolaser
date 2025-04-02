export type Material = 
    'stainless-steel' |
    'aluminum' |
    'brass' |
    'copper' |
    'gold' |
    'silver' |
    'marble' |
    'coastal-stone';

export interface MaterialConfig {
    roughness: number;
    metalness: number;
    color: string;
    textureUrl: string;
    normalMapUrl: string;
}

export const MATERIALS: Record<MaterialType, MaterialConfig> ={
    'stainless-steel': {
        roughness: 0.3,
        metalness: 0.9,
        color: '#d4d4d4',
        textureUrl: '/textures/metals/stainless_steel_diffuse.jpg',
        normalMapUrl: '/textures/metals/stainless_steel_normal.jpg'
    },
    'gold': {
        roughness: 0.25,
        metalness: 0.95,
        color: '#FFD700',
        textureUrl: '/textures/metals/gold_diffuse.jpg'
    },
    'silver': {
        roughness: 0.3,
        metalness: 0.8,
        color: '#C0C0C0',
        textureUrl: '/textures/metals/silver_diffuse.jpg'
    },
    'bronze':
    {
        roughness: 0.4,
        metalness: 0.85,
        color: '#CD7F32',
        textureUrl: '/textures/metals/bronze_diffuse.jpg'
    },
    'brass':{
        roughness: 0.35,
        metalness: 0.9,
        color: '#b5a642',
    },
    'marble': {
        roughness: 0.6,
        netakbess: 0.1,
        color: '#ffffff',
        textureUrl: '/textures/marbles/marble_diffuse.jpg',
        normalMapUrl: '/textures/marbles/marble_normal.jpg'
    },
    'coastal-stone': {
        roughness: 0.8,
        metalness: 0.05,
        color: '#a89f8e',
        textureUrl: '/textures/rocks/coastal_stone_diffuse.jpg',
        normalMapUrl: '/textures/rocks/coastal_stone_normal.jpg'
    },
}