"""
Template Adapter for GPT-4o Image Prompts Gallery
Adapts the 333 GPT-4o prompt templates for ComfyUI nodes
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


class PromptTemplateAdapter:
    """
    Adapter for GPT-4o Image Prompts (333 cases)
    Provides bilingual template browsing and category management
    """
    
    def __init__(self):
        """Initialize adapter and load templates"""
        self.base_dir = Path(__file__).parent
        self.data_file = self.base_dir / "gpt4o-image-prompts-master" / "gpt4o-image-prompts-master" / "data" / "prompts.json"
        self.templates = []
        self.categories = {}
        self._load_templates()
    
    def _load_templates(self):
        """Load templates from prompts.json"""
        try:
            if not self.data_file.exists():
                print(f"[PromptTemplateAdapter] Warning: Data file not found: {self.data_file}")
                return
            
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'items' in data:
                self.templates = data['items']
                print(f"[PromptTemplateAdapter] Loaded {len(self.templates)} templates")
                self._build_categories()
            else:
                print(f"[PromptTemplateAdapter] Warning: No 'items' found in data file")
        
        except Exception as e:
            print(f"[PromptTemplateAdapter] Error loading templates: {e}")
            import traceback
            traceback.print_exc()
    
    def _build_categories(self):
        """Build category index from templates"""
        # Collect all unique tags
        all_tags = set()
        for template in self.templates:
            tags = template.get('tags', [])
            all_tags.update(tags)
        
        # Build category dictionary
        for tag in sorted(all_tags):
            self.categories[tag] = {
                'id': tag,
                'name_zh': self._translate_tag_zh(tag),
                'name_en': tag.replace('-', ' ').title(),
                'count': sum(1 for t in self.templates if tag in t.get('tags', []))
            }
    
    def _translate_tag_zh(self, tag: str) -> str:
        """Translate English tag to Chinese"""
        translations = {
            # 基础类型
            'portrait': '人像',
            'landscape': '风景',
            'interior': '室内',
            'nature': '自然',
            'photography': '摄影',
            'illustration': '插画',
            'logo': '标志',
            'minimalist': '极简',
            'character': '角色',
            'branding': '品牌',
            'poster': '海报',
            'ui': '界面',
            
            # 工艺材质
            'paper-craft': '纸艺',
            'clay': '粘土',
            'felt': '毛毡',
            'sculpture': '雕塑',
            'pixel': '像素',
            
            # 对象主题
            'toy': '玩具',
            'vehicle': '交通工具',
            'architecture': '建筑',
            'food': '美食',
            'product': '产品',
            'animal': '动物',
            'fashion': '时尚',
            
            # 风格流派
            'abstract': '抽象',
            'pattern': '图案',
            'typography': '字体',
            'vintage': '复古',
            'retro': '复古',
            'modern': '现代',
            'fantasy': '奇幻',
            'scifi': '科幻',
            'futuristic': '未来',
            'neon': '霓虹',
            'cyberpunk': '赛博朋克',
            
            # 艺术形式
            'anime': '动漫',
            'cartoon': '卡通',
            '3d': '三维',
            'pixel-art': '像素艺术',
            'watercolor': '水彩',
            'oil-painting': '油画',
            'sketch': '素描',
            
            # 其他
            'emoji': '表情',
            'infographic': '信息图',
            'gaming': '游戏',
            'creative': '创意',
        }
        return translations.get(tag, tag)
    
    def get_all_categories(self, lang: str = 'zh') -> List[Dict[str, Any]]:
        """
        Get all template categories
        
        Args:
            lang: Language code ('zh' or 'en')
        
        Returns:
            List of category dictionaries
        """
        result = []
        for cat_id, cat_data in self.categories.items():
            name_key = 'name_zh' if lang == 'zh' else 'name_en'
            result.append({
                'id': cat_id,
                'name': cat_data[name_key],
                'count': cat_data['count']
            })
        
        # Sort by count descending
        result.sort(key=lambda x: x['count'], reverse=True)
        return result
    
    def get_templates_by_category(self, category_id: str) -> List[Dict[str, Any]]:
        """
        Get templates filtered by category
        
        Args:
            category_id: Category/tag ID
        
        Returns:
            List of template dictionaries
        """
        filtered = []
        
        for template in self.templates:
            if category_id in template.get('tags', []):
                # Extract both language prompts if available
                prompts = template.get('prompts', [])
                
                # Handle description - convert string to bilingual object
                desc = template.get('description', '')
                desc_obj = {
                    'zh': desc if desc else '',
                    'en': desc if desc else ''
                }
                
                prompt_data = {
                    'id': template.get('id'),
                    'title': template.get('title', ''),
                    'description': desc_obj,
                    'tags': template.get('tags', []),
                    'coverImage': template.get('coverImage', ''),
                    'images': template.get('images', []),
                    'prompt': {
                        'zh': prompts[1] if len(prompts) > 1 else prompts[0] if prompts else '',
                        'en': prompts[0] if prompts else ''
                    },
                    'source': template.get('source', {}),
                    'notes': template.get('notes', []),
                    'examples': template.get('examples', []),
                    'difficulty': template.get('difficulty', '')
                }
                
                filtered.append(prompt_data)
        
        # Sort by ID descending (newest first)
        filtered.sort(key=lambda x: x['id'], reverse=True)
        return filtered
    
    def get_template_by_id(self, template_id: int) -> Dict[str, Any]:
        """
        Get a specific template by ID
        
        Args:
            template_id: Template ID
        
        Returns:
            Template dictionary or None
        """
        for template in self.templates:
            if template.get('id') == template_id:
                prompts = template.get('prompts', [])
                
                # Handle description - convert string to bilingual object
                desc = template.get('description', '')
                desc_obj = {
                    'zh': desc if desc else '',
                    'en': desc if desc else ''
                }
                
                return {
                    'id': template.get('id'),
                    'title': template.get('title', ''),
                    'description': desc_obj,
                    'tags': template.get('tags', []),
                    'coverImage': template.get('coverImage', ''),
                    'images': template.get('images', []),
                    'prompt': {
                        'zh': prompts[1] if len(prompts) > 1 else prompts[0] if prompts else '',
                        'en': prompts[0] if prompts else ''
                    },
                    'source': template.get('source', {}),
                    'notes': template.get('notes', []),
                    'examples': template.get('examples', []),
                    'difficulty': template.get('difficulty', '')
                }
        return None
    
    def search_templates(self, keyword: str, lang: str = 'zh') -> List[Dict[str, Any]]:
        """
        Search templates by keyword
        
        Args:
            keyword: Search keyword
            lang: Language for search
        
        Returns:
            List of matching templates
        """
        keyword_lower = keyword.lower()
        results = []
        
        for template in self.templates:
            # Search in title
            if keyword_lower in template.get('title', '').lower():
                prompts = template.get('prompts', [])
                
                # Handle description - convert string to bilingual object
                desc = template.get('description', '')
                desc_obj = {
                    'zh': desc if desc else '',
                    'en': desc if desc else ''
                }
                
                results.append({
                    'id': template.get('id'),
                    'title': template.get('title', ''),
                    'description': desc_obj,
                    'tags': template.get('tags', []),
                    'coverImage': template.get('coverImage', ''),
                    'prompt': {
                        'zh': prompts[1] if len(prompts) > 1 else prompts[0] if prompts else '',
                        'en': prompts[0] if prompts else ''
                    },
                    'difficulty': template.get('difficulty', '')
                })
        
        return results


# For backward compatibility
if __name__ == "__main__":
    # Test the adapter
    adapter = PromptTemplateAdapter()
    print(f"Loaded {len(adapter.templates)} templates")
    print(f"Categories: {len(adapter.categories)}")
    
    # Test get categories
    categories = adapter.get_all_categories('zh')
    print(f"\nTop 5 categories:")
    for cat in categories[:5]:
        print(f"  - {cat['name']} ({cat['count']})")
    
    # Test get templates by category
    if categories:
        first_cat = categories[0]
        templates = adapter.get_templates_by_category(first_cat['id'])
        print(f"\nTemplates in '{first_cat['name']}': {len(templates)}")
        if templates:
            print(f"First template: {templates[0]['title']}")

